#!/usr/bin/env python3
"""
zonebuild -- turn a readable zone spec into CircleMUD 3.1 world files.

A spec is a Python module in tools/zonebuild/zones/ defining ZONE (a dict).
Rooms, mobs and objects use short local ids; the builder assigns vnums in
order from the zone's base, writes lib/world/{wld,mob,obj,zon}/<num>.*, adds
the files to each index, and derives every mob's stats from the scaling rules
in the World Zone Plan (role + level -> hp, damage, hitroll, AC, exp, gold).

    python3 tools/zonebuild/zonebuild.py <spec name> [<spec name> ...]
    python3 tools/zonebuild/zonebuild.py --check <spec name>   (validate only)

Spec format (all keys optional unless noted):

ZONE = {
  'num': 200, 'name': 'The Burned Marches', 'builders': 'Claude',     # required
  'lifespan': 20, 'reset_mode': 2,
  'rooms': [ {'id': 'gate', 'name': '...', 'desc': '...',            # required
              'sector': 'field', 'flags': 'd',                       # room flag letters
              'exits': {'n': 'tower'                                 # local id
                        'w': '@3052',                                # vnum outside the zone
                        'e': {'to': 'yard', 'door': 'gate', 'desc': '...',
                              'key': 'iron_key', 'state': 'locked', 'oneway': True}},
              'extras': {'statue carving': 'text'},
              'mobs': [('ghoul', 2)],                                # (mob id, max in world)
              'objs': [('altar', 1)] } ],                            # objects on the floor
  'mobs': [ {'id': 'ghoul', 'aliases': 'ghoul', 'short': 'a ghoul', 'long': '...',
             'desc': '...', 'role': 'standard', 'level': 33, 'flags': 'f', 'aff': '',
             'align': -800, 'attack': 'claw', 'sex': 0,
             'equip': [('rusty_blade', 'wield', 50)],                # (obj id, slot, load %)
             'carry': [('bone_charm', 25)]} ],
  'objs': [ {'id': 'rusty_blade', 'kind': 'weapon', 'level': 33, 'attack': 'slash',
             'aliases': '...', 'short': '...', 'long': '...', ...} ],
}

Exits are two-way by default: the builder adds the reverse exit inside the
zone unless the exit says 'oneway' or the other room already has one there.
"""
import os, re, sys, textwrap, importlib.util

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORLD = os.path.join(ROOT, 'lib', 'world')
SPECS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zones')

DIRS = {'n': 0, 'e': 1, 's': 2, 'w': 3, 'u': 4, 'd': 5}
REV = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', 'u': 'd', 'd': 'u'}
# 'water' = wadeable/swimmable (SECT_WATER_SWIM); 'deepwater' needs a boat (SECT_WATER_NOSWIM).
SECTORS = {'inside': 0, 'city': 1, 'field': 2, 'forest': 3, 'hills': 4, 'mountain': 5,
           'swim': 6, 'water': 6, 'deepwater': 7, 'flying': 8, 'underwater': 9}
WEAR_POS = {'light': 0, 'finger': 1, 'neck': 3, 'body': 5, 'head': 6, 'legs': 7, 'feet': 8,
            'hands': 9, 'arms': 10, 'shield': 11, 'about': 12, 'waist': 13, 'wrist': 14,
            'wield': 16, 'hold': 17}
# ITEM_WEAR_* bits; every wearable also gets TAKE (1).
WEAR_BITS = {'finger': 2, 'neck': 4, 'body': 8, 'head': 16, 'legs': 32, 'feet': 64, 'hands': 128,
             'arms': 256, 'shield': 512, 'about': 1024, 'waist': 2048, 'wrist': 4096,
             'wield': 8192, 'hold': 16384}
ATTACKS = {'hit': 0, 'sting': 1, 'whip': 2, 'slash': 3, 'bite': 4, 'bludgeon': 5, 'crush': 6,
           'pound': 7, 'claw': 8, 'maul': 9, 'thrash': 10, 'pierce': 11, 'blast': 12,
           'punch': 13, 'stab': 14}
APPLY = {'str': 1, 'dex': 2, 'int': 3, 'wis': 4, 'con': 5, 'cha': 6, 'mana': 12, 'hit': 13, 'move': 14,
         'ac': 17, 'hitroll': 18, 'damroll': 19, 'save_para': 20, 'save_spell': 24}
ITEM_TYPES = {'light': 1, 'scroll': 2, 'wand': 3, 'staff': 4, 'weapon': 5, 'treasure': 8,
              'armor': 9, 'potion': 10, 'worn': 11, 'other': 12, 'container': 15, 'note': 16,
              'drinkcon': 17, 'key': 18, 'food': 19, 'money': 20, 'fountain': 23}
DOOR_STATE = {'open': 0, 'closed': 1, 'locked': 2}


class SpecError(Exception):
    pass


# ---------------------------------------------------------------- scaling
#
# Player baselines (World Zone Plan, "Difficulty and mob scaling"): a level-L
# character has about 14*L hp and deals about 0.7*L + 5 damage a round; a
# level-100 warrior measured ~1,550 hp and ~4 swings a round.
ROLE = {
    #            rounds-to-kill  players  dmg % of player hp/round  level bonus  exp x
    'standard': (10,             1,       0.04,                     0,           1),
    'elite':    (25,             1,       0.075,                    0,           3),
    'champion': (35,             2.5,     0.12,                     3,           10),
    'boss':     (50,             4,       0.175,                    5,           30),
    'harmless': (3,              1,       0.0,                      0,           0.2),
    # W15 only: the Entity, for a full group of remorted level-100 characters
    'entity':   (80,             5,       0.22,                     10,          60),
}
HP_CAP = 32000            # sh_int max_hit
DICE_CAP = 255            # damage dice are stored in a byte


def player_hp(level):
    return 14 * level


def player_dpr(level):
    return 0.7 * level + 5


def mob_stats(role, level):
    if role not in ROLE:
        raise SpecError('unknown role %r' % role)
    rounds, players, dmg_pct, lv_bonus, exp_x = ROLE[role]
    lv = max(1, level + lv_bonus)
    hp = int(min(HP_CAP, max(10, rounds * players * player_dpr(level))))
    # hp as XdY+Z: a small random spread around the target
    hd_n, hd_s = max(1, lv // 4), 10
    hp_bonus = max(1, hp - hd_n * (hd_s + 1) // 2)
    # damage per round = a share of one player's hp at this level.  damroll is a
    # signed byte (max 127), so the bonus is held to a third and dice carry the rest.
    dpr = max(1.0, dmg_pct * player_hp(level))
    dbonus = int(min(100, dpr / 3))
    dn = max(1, min(DICE_CAP, lv // 10 + 1))
    ds = max(2, min(DICE_CAP, round(2 * (dpr - dbonus) / dn - 1)))
    if role == 'harmless':
        dn, ds, dbonus = 1, 2, 0
    thac0 = max(0, 20 - lv // 4)
    ac = max(-10, 10 - lv // 8)
    exp = int(exp_x * (lv ** 2) * 12 + 10)
    gold = int((lv ** 1.6) * (1 + exp_x / 5))
    return dict(level=lv, thac0=thac0, ac=ac, hp=(hd_n, hd_s, hp_bonus),
                dam=(dn, ds, dbonus), exp=exp, gold=gold)


def weapon_dice(level, two_handed=False):
    avg = 2.5 + level * 0.11 + (1.5 if two_handed else 0)       # level 100 ~ 13.5 average
    n = max(1, round(avg / 3.5))
    s = max(2, round(2 * avg / n - 1))
    return n, s


def armor_value(level, slot):
    base = {'body': 10, 'shield': 8, 'head': 6, 'legs': 6, 'arms': 5, 'about': 5,
            'hands': 4, 'feet': 4, 'waist': 3, 'wrist': 2, 'neck': 2, 'finger': 1}.get(slot, 3)
    return max(1, round(base * (0.4 + level / 60)))


# ---------------------------------------------------------------- text
def wrap_desc(text):
    """CircleMUD room style: paragraphs indented 3 spaces, wrapped at 76."""
    paras = [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    out = []
    for p in paras:
        p = ' '.join(p.split())
        out.append(textwrap.fill(p, 76, initial_indent='   ', subsequent_indent=''))
    return '\n'.join(out)


def wrap_plain(text):
    paras = [' '.join(p.split()) for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    return '\n'.join(textwrap.fill(p, 76) for p in paras)


def clean(s, where):
    if '~' in s:
        raise SpecError('%s contains a ~' % where)
    return s


# ---------------------------------------------------------------- build
def load_spec(name):
    path = os.path.join(SPECS, name if name.endswith('.py') else name + '.py')
    sp = importlib.util.spec_from_file_location('zone_' + os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod.ZONE


def existing_rooms():
    rooms = set()
    for f in os.listdir(os.path.join(WORLD, 'wld')):
        if f.endswith('.wld'):
            for v in re.findall(r'^#(\d+)$', open(os.path.join(WORLD, 'wld', f), encoding='latin-1').read(), re.M):
                rooms.add(int(v))
    return rooms


def build(zone, world_rooms, write=True):
    num = zone['num']
    base = num * 100
    top = zone.get('top', base + 99)
    errs = []
    rooms, mobs, objs = zone['rooms'], zone.get('mobs', []), zone.get('objs', [])
    rid = {r['id']: base + i for i, r in enumerate(rooms)}
    mid = {m['id']: base + i for i, m in enumerate(mobs)}
    oid = {o['id']: base + i for i, o in enumerate(objs)}
    for kind, d in (('room', rid), ('mob', mid), ('obj', oid)):
        if len(d) != len(set(d)):
            errs.append('duplicate %s ids' % kind)
        if d and max(d.values()) > top:
            errs.append('too many %ss for vnums %d-%d' % (kind, base, top))
    ids = {r['id'] for r in rooms}
    if len(ids) != len(rooms):
        errs.append('duplicate room ids')

    # ----- exits, with automatic reverse exits
    exits = {r['id']: {} for r in rooms}
    for r in rooms:
        for d, e in r.get('exits', {}).items():
            if d not in DIRS:
                errs.append('room %s: bad direction %r' % (r['id'], d)); continue
            e = {'to': e} if isinstance(e, str) else dict(e)
            exits[r['id']][d] = e
    for r in rooms:
        for d, e in list(exits[r['id']].items()):
            to = e['to']
            if to.startswith('@'):
                v = int(to[1:])
                if v not in world_rooms and not (base <= v <= top):
                    errs.append('room %s exit %s: vnum %d does not exist' % (r['id'], d, v))
                continue
            if to not in rid:
                errs.append('room %s exit %s: unknown room %r' % (r['id'], d, to)); continue
            if e.get('oneway'):
                continue
            back = exits[to].get(REV[d])
            if back is None:
                rev = {'to': r['id']}
                for k in ('door', 'key', 'state'):
                    if k in e:
                        rev[k] = e[k]
                if 'back_desc' in e:
                    rev['desc'] = e['back_desc']
                exits[to][REV[d]] = rev
            elif back['to'] != r['id']:
                errs.append('room %s exit %s -> %s, but %s exit %s -> %s' %
                            (r['id'], d, to, to, REV[d], back['to']))

    # ----- validate references
    for r in rooms:
        for m, n in r.get('mobs', []):
            if m not in mid: errs.append('room %s loads unknown mob %r' % (r['id'], m))
        for entry in r.get('objs', []):
            for o in [entry[0]] + [x[0] for x in (entry[2] if len(entry) > 2 else [])]:
                if o not in oid: errs.append('room %s loads unknown obj %r' % (r['id'], o))
        for k in ('name', 'desc'):
            if not r.get(k): errs.append('room %s has no %s' % (r['id'], k))
        if len(r.get('desc', '')) < 120:
            errs.append('room %s: description under 120 characters' % r['id'])
    for m in mobs:
        for o, slot, pct in m.get('equip', []):
            if o not in oid: errs.append('mob %s equips unknown obj %r' % (m['id'], o))
            if slot not in WEAR_POS: errs.append('mob %s: bad slot %r' % (m['id'], slot))
        for o, pct in m.get('carry', []):
            if o not in oid: errs.append('mob %s carries unknown obj %r' % (m['id'], o))
    for r in rooms:
        for d, e in exits[r['id']].items():
            if 'key' in e and e['key'] not in oid and not str(e['key']).lstrip('-').isdigit():
                errs.append('room %s exit %s: unknown key %r' % (r['id'], d, e['key']))
    for o in objs:
        for loc, mod in o.get('affects', []):
            if loc not in APPLY: errs.append('obj %s: unknown affect %r' % (o['id'], loc))
    if errs:
        raise SpecError('\n'.join(errs))

    # ----- exits other zones patched into our rooms (kept across rebuilds)
    kept = {}
    old_path = os.path.join(WORLD, 'wld', '%d.wld' % num)
    if os.path.exists(old_path):
        old = open(old_path, encoding='latin-1').read()
        for blk in re.split(r'\n(?=#\d+\n)', '\n' + old):
            m = re.match(r'\s*#(\d+)\n', blk)
            if not m:
                continue
            for ex in re.finditer(r'\nD(\d)[ \t]*\n((?:[^\n]*\n)*?)([^\n]*~)\n([^\n]*~)\n(-?\d+) (-?\d+) (-?\d+)', blk):
                to = int(ex.group(7))
                if not (base <= to <= top) and to != -1:
                    kept.setdefault(int(m.group(1)), {})[int(ex.group(1))] = ex.group(0).lstrip('\n')
    declared = {(rid[r['id']], DIRS[d]) for r in rooms for d in exits[r['id']]}

    # ----- rooms
    w = []
    for r in rooms:
        w.append('#%d\n%s~\n%s\n~\n%d %s %d' % (rid[r['id']], clean(r['name'], 'room name'),
                 clean(wrap_desc(r['desc']), 'room desc'), num, r.get('flags', '0') or '0',
                 SECTORS[r.get('sector', 'field')]))
        for d in 'neswud':
            e = exits[r['id']].get(d)
            if not e:
                continue
            to = int(e['to'][1:]) if e['to'].startswith('@') else rid[e['to']]
            door = e.get('door')
            info = 0 if not door else (2 if e.get('pickproof') else 1)
            key = e.get('key', -1)
            key = oid[key] if key in oid else int(key)
            edesc = clean(wrap_plain(e.get('desc', '')), 'exit desc')
            w.append('D%d\n%s~\n%s~\n%d %d %d' % (DIRS[d], edesc + '\n' if edesc else '',
                     door or '', info, key, to))
        for dnum, block in sorted(kept.get(rid[r['id']], {}).items()):
            if (rid[r['id']], dnum) not in declared:      # patched in by another zone
                w.append(block)
        for kw, text in r.get('extras', {}).items():
            w.append('E\n%s~\n%s\n~' % (kw, clean(wrap_plain(text), 'extra')))
        w.append('S')
    w.append('$')

    # ----- mobs
    mb = []
    for m in mobs:
        st = mob_stats(m.get('role', 'standard'), m['level'])
        flags = 'd' + m.get('flags', '')            # d = ISNPC, always
        if 'b' not in flags and 'g' not in flags:   # wanderers never leave their zone
            flags += 'g'
        aff = m.get('aff', '') or '0'
        long = m['long'].rstrip()
        if not long.endswith(('.', '!', '?')):
            raise SpecError('mob %s long line should end with punctuation' % m['id'])
        mb.append('#%d\n%s~\n%s~\n%s\n~\n%s\n~\n%s %s %d E\n%d %d %d %dd%d+%d %dd%d+%d\n%d %d\n%d %d %d'
                  % (mid[m['id']], m['aliases'], m['short'], long, wrap_plain(m['desc']),
                     flags, aff, m.get('align', 0), st['level'], st['thac0'], st['ac'],
                     *st['hp'], *st['dam'], m.get('gold', st['gold']), st['exp'],
                     8, 8, m.get('sex', 0)))
        mb.append('BareHandAttack: %d' % ATTACKS[m.get('attack', 'hit')])
        for k, v in m.get('abils', {}).items():
            mb.append('%s: %d' % (k, v))
        mb.append('E')
    mb.append('$')

    # ----- objects
    ob = []
    for o in objs:
        kind = o['kind']
        lvl = o.get('level', 1)
        extra = o.get('extra', '0') or '0'
        wear = 1
        vals = [0, 0, 0, 0]
        affects = list(o.get('affects', []))
        if kind == 'weapon':
            n, s = o.get('dice') or weapon_dice(lvl, o.get('two_handed', False))
            vals = [0, n, s, ATTACKS[o.get('attack', 'slash')]]
            wear |= WEAR_BITS['wield']
        elif kind == 'armor':
            vals = [o.get('ac', armor_value(lvl, o['slot'])), 0, 0, 0]
            wear |= WEAR_BITS[o['slot']]
        elif kind == 'worn':
            wear |= WEAR_BITS[o['slot']]
        elif kind == 'light':
            vals = [0, 0, o.get('hours', -1), 0]
            wear |= WEAR_BITS['hold']
        elif kind == 'container':
            vals = [o.get('capacity', 50), o.get('cflags', 0), -1, 0]
            if o.get('fixed'): wear = 0
        elif kind == 'drinkcon':
            vals = [o.get('capacity', 10), o.get('capacity', 10), o.get('liquid', 0), 0]
            wear |= WEAR_BITS['hold']
        elif kind == 'fountain':
            vals = [100, 100, o.get('liquid', 0), 0]; wear = 0
        elif kind == 'food':
            vals = [o.get('hours', 8), 0, 0, 0]
        elif kind == 'potion':
            sp = [x if x else -1 for x in o.get('spells', [])] + [-1, -1, -1]   # -1 = no spell
            vals = [o.get('spell_level', lvl), sp[0], sp[1], sp[2]]
        elif kind == 'key':
            vals = [0, 0, 0, 0]
        elif kind in ('treasure', 'other', 'note'):
            if o.get('slot'): wear |= WEAR_BITS[o['slot']]
        if o.get('fixed'):
            wear = 0
        if o.get('wear') is not None:
            wear = o['wear']
        weight = o.get('weight', {'weapon': 8, 'armor': 10, 'container': 5}.get(kind, 2))
        cost = o.get('cost', int(10 + lvl ** 1.7))
        ob.append('#%d\n%s~\n%s~\n%s~\n~\n%d %s %d\n%d %d %d %d\n%d %d %d'
                  % (oid[o['id']], o['aliases'], o['short'], o['long'], ITEM_TYPES[kind], extra, wear,
                     *vals, weight, cost, max(1, cost // 10)))
        for kw, text in o.get('extras', {}).items():
            ob.append('E\n%s~\n%s\n~' % (kw, clean(wrap_plain(text), 'obj extra')))
        if len(affects) > 6:
            raise SpecError('obj %s has more than 6 affects' % o['id'])
        for loc, mod in affects:
            ob.append('A\n%d %d' % (APPLY[loc], mod))
    ob.append('$')

    # ----- zone resets
    z = ['#%d' % num, '%s~' % zone.get('builders', 'Claude'), '%s~' % zone['name'],
         '%d %d %d %d' % (base, top, zone.get('lifespan', 20), zone.get('reset_mode', 2))]
    for r in rooms:
        for entry in r.get('objs', []):
            o, n = entry[0], entry[1]
            z.append('O 0 %d %d %d\t%s' % (oid[o], n, rid[r['id']], o))
            for inner, k in (entry[2] if len(entry) > 2 else []):   # contents: P commands
                z.append('P 1 %d %d %d\t%s' % (oid[inner], k, oid[o], inner))
        for m, n in r.get('mobs', []):
            z.append('M 0 %d %d %d\t%s' % (mid[m], n, rid[r['id']], m))
            spec = next(x for x in mobs if x['id'] == m)
            for o, slot, pct in spec.get('equip', []):
                z.append('E 1 %d %d %d\t%s' % (oid[o], pct, WEAR_POS[slot], o))
            for o, pct in spec.get('carry', []):
                z.append('G 1 %d %d\t%s' % (oid[o], pct, o))
        for d, e in exits[r['id']].items():
            if e.get('door') and e.get('state', 'closed') != 'open':
                z.append('D 0 %d %d %d' % (rid[r['id']], DIRS[d], DOOR_STATE[e.get('state', 'closed')]))
    z += ['S', '$']

    files = {'wld': '\n'.join(w) + '\n', 'mob': '\n'.join(mb) + '\n',
             'obj': '\n'.join(ob) + '\n', 'zon': '\n'.join(z) + '\n'}
    if write:
        for ext, text in files.items():
            if ext in ('mob', 'obj') and text == '$\n':
                continue
            with open(os.path.join(WORLD, ext, '%d.%s' % (num, ext)), 'w') as f:
                f.write(text)
            add_to_index(ext, '%d.%s' % (num, ext))
        apply_links(zone, rid)
    return dict(rooms=len(rooms), mobs=len(mobs), objs=len(objs), vnums=rid)


def _room_file(vnum):
    wdir = os.path.join(WORLD, 'wld')
    for f in os.listdir(wdir):
        if f.endswith('.wld'):
            p = os.path.join(wdir, f)
            if re.search(r'^#%d$' % vnum, open(p, encoding='latin-1').read(), re.M):
                return p
    raise SpecError('room %d not found in any .wld file' % vnum)


def set_exit(vnum, d, to, desc='', keyword='', info=0, key=-1):
    """Write (or replace) one exit of an existing room in another zone's file.
    to=None removes the exit."""
    path = _room_file(vnum)
    text = open(path, encoding='latin-1').read()
    m = re.search(r'^#%d\n.*?^S$' % vnum, text, re.M | re.S)
    block = m.group(0)
    ex = re.compile(r'^D%d[ \t]*\n(?:[^\n]*\n)*?[^\n]*~\n[^\n]*~\n-?\d+ -?\d+ -?\d+\n' % DIRS[d], re.M)
    block2 = ex.sub('', block)
    if to is not None:
        dtext = wrap_plain(desc)
        new = 'D%d\n%s~\n%s~\n%d %d %d\n' % (DIRS[d], dtext + '\n' if dtext else '', keyword, info, key, to)
        # exits go before the first extra description / the closing S
        cut = re.search(r'^(E|S)$', block2, re.M).start()
        block2 = block2[:cut] + new + block2[cut:]
    if block2 != block:
        open(path, 'w', encoding='latin-1').write(text[:m.start()] + block2 + text[m.end():])


def set_room_desc(vnum, desc):
    """Replace an existing room's description (used when a new zone changes what it looks onto)."""
    path = _room_file(vnum)
    text = open(path, encoding='latin-1').read()
    m = re.search(r'^(#%d\n[^\n]*~\n)(.*?\n)~\n' % vnum, text, re.M | re.S)
    if not m:
        raise SpecError('room %d: cannot find its description' % vnum)
    text = text[:m.start(2)] + wrap_desc(desc) + '\n' + text[m.end(2):]
    open(path, 'w', encoding='latin-1').write(text)


def apply_links(zone, vnums):
    """Patch rooms outside the zone: reverse exits, removed exits, new descriptions."""
    for r in zone['rooms']:
        for d, e in r.get('exits', {}).items():
            e = {'to': e} if isinstance(e, str) else e
            if e['to'].startswith('@') and not e.get('oneway'):
                v = int(e['to'][1:])
                set_exit(v, REV[d], vnums[r['id']], e.get('back_desc', ''), e.get('door', ''),
                         1 if e.get('door') else 0, -1)
    for v, d in zone.get('remove_exits', []):
        set_exit(v, d, None)
    for v, desc in zone.get('room_descs', {}).items():
        set_room_desc(v, desc)


def add_to_index(ext, fname):
    path = os.path.join(WORLD, ext, 'index')
    lines = [l.strip() for l in open(path) if l.strip()]
    if fname in lines:
        return
    lines = [l for l in lines if l != '$']
    lines.append(fname)
    def key(f):
        m = re.match(r'(\d+)\.', f)
        return int(m.group(1)) if m else 10 ** 9
    lines.sort(key=key)
    with open(path, 'w') as f:
        f.write('\n'.join(lines + ['$']) + '\n')


def main(argv):
    check = '--check' in argv
    names = [a for a in argv if not a.startswith('--')]
    world = existing_rooms()
    for n in names:
        zone = load_spec(n)
        info = build(zone, world, write=not check)
        world |= set(info['vnums'].values())
        print('%s zone %d %s: %d rooms, %d mobs, %d objs' %
              ('checked' if check else 'built', zone['num'], zone['name'], info['rooms'], info['mobs'], info['objs']))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except SpecError as e:
        print('SPEC ERROR:\n' + str(e)); sys.exit(1)
