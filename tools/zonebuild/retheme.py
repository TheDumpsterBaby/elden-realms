#!/usr/bin/env python3
"""Re-theme existing CircleMUD zones in place.

Unlike zonebuild.py, which writes whole new zones, this rewrites the *text*
of rooms, mobs and objects that already exist -- names, descriptions, extra
descriptions, exit descriptions -- and leaves exits, flags, stats, shops and
spec procs alone.  It can also append new mobs/objects to an existing zone
(stats from zonebuild's scaling rules) and add reset commands for them.

Spec (tools/zonebuild/retheme/<name>.py) defines RETHEME = {
    'zones':  {30: 'The Fort of Midgaard'},                 # zone names
    'rooms':  {3001: {'name': ..., 'desc': ..., 'extras': {kw: text},
                      'exits': {'n': 'exit desc'}}},
    'mobs':   {3060: {'aliases': ..., 'short': ..., 'long': ..., 'desc': ...}},
    'objs':   {3020: {'aliases': ..., 'short': ..., 'long': ..., 'extras': {...}}},
    'new_mobs': [{'vnum': 3011, 'zone': 30, ...zonebuild mob keys...}],
    'new_objs': [{'vnum': 3011, 'zone': 30, ...zonebuild obj keys...}],
    'resets': {30: ['M 0 3011 2 3040', 'E 1 3011 100 16']},  # appended before S
    'remove_resets': {30: ['M 0 3062 ']},                  # drop lines starting so
}
Usage: retheme.py <spec> [--check]
"""
import importlib.util
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zonebuild as zb  # noqa: E402

WORLD = zb.WORLD
DIRN = zb.DIRS


def blocks(text):
    """Split a world file into (vnum, block) pieces; trailing '$' kept separately."""
    parts = re.split(r'(?m)^(?=#\d+\s*$)', text)
    head, out = parts[0], []
    for p in parts[1:]:
        v = int(re.match(r'#(\d+)', p).group(1))
        out.append([v, p])
    return head, out


def zone_of(vnum):
    """Which file holds vnum: the zone whose range covers it."""
    for f in os.listdir(os.path.join(WORLD, 'zon')):
        if not f.endswith('.zon'):
            continue
        with open(os.path.join(WORLD, 'zon', f)) as fh:
            lines = fh.read().split('\n')
        lo, hi = map(int, lines[3].split()[:2])
        if lo <= vnum <= hi:
            return int(f[:-4])
    raise zb.SpecError('no zone holds vnum %d' % vnum)


def tilde(s, where):
    return zb.clean(s, where)


def redo_room(block, r, vnum):
    lines = block.split('\n')
    # lines[0] '#v', [1] name~, desc lines until a line ending '~'
    i = 2
    while not lines[i].endswith('~'):
        i += 1
    rest = lines[i + 1:]
    if lines[i] != '~':                 # desc ended "text~": keep the text when not replaced
        pass
    name = tilde(r.get('name', lines[1][:-1]), 'room %d name' % vnum) + '~'
    if 'desc' in r:
        desc = zb.wrap_desc(tilde(r['desc'], 'room %d desc' % vnum)) + '\n~'
    else:
        desc = '\n'.join(lines[2:i + 1])
    body = '\n'.join(rest)
    for d, text in r.get('exits', {}).items():
        n = DIRN[d]
        m = re.search(r'(?ms)^D%d[ \t]*\n(.*?)~\n' % n, body)
        if not m:
            raise zb.SpecError('room %d has no exit %s' % (vnum, d))
        body = body[:m.start(1)] + (zb.wrap_plain(tilde(text, 'exit')) + '\n') + body[m.end(1):]
    if 'extras' in r:
        # drop old E blocks, put the new ones just before the final S
        body = re.sub(r'(?ms)^E\n[^\n]*~\n.*?^~\n', '', body)
        ex = ''.join('E\n%s~\n%s\n~\n' % (kw, zb.wrap_plain(tilde(t, 'extra'))) for kw, t in r['extras'].items())
        body = re.sub(r'(?m)^S\s*$', lambda _: ex + 'S', body, count=1)
    return '\n'.join([lines[0], name, desc]) + '\n' + body


def redo_mob(block, m, vnum):
    lines = block.split('\n')
    # #v, aliases~, short~, long..., '~', desc..., '~', rest
    i = 3
    while lines[i] != '~' and not lines[i].endswith('~'):
        i += 1
    j = i + 1
    while lines[j] != '~' and not lines[j].endswith('~'):
        j += 1
    al = tilde(m.get('aliases', lines[1][:-1]), 'mob alias') + '~'
    sh = tilde(m.get('short', lines[2][:-1]), 'mob short') + '~'
    lo = (tilde(m['long'], 'mob long').strip() + '\n~') if 'long' in m else '\n'.join(lines[3:i + 1])
    de = (zb.wrap_plain(tilde(m['desc'], 'mob desc')) + '\n~') if 'desc' in m else '\n'.join(lines[i + 1:j + 1])
    rest = lines[j + 1:]
    if 'align' in m:
        f = rest[0].split()
        f[2] = str(m['align'])
        rest[0] = ' '.join(f)
    return '\n'.join([lines[0], al, sh, lo, de] + rest)


def redo_obj(block, o, vnum):
    lines = block.split('\n')
    # #v, aliases~, short~, long~ (may span lines), action~ (may span), rest
    def take(k):
        s = k
        while not lines[k].endswith('~'):
            k += 1
        return s, k
    a = 1
    s = 2
    l0, l1 = take(3)
    c0, c1 = take(l1 + 1)
    al = tilde(o.get('aliases', lines[a][:-1]), 'obj alias') + '~'
    sh = tilde(o.get('short', lines[s][:-1]), 'obj short') + '~'
    lo = (tilde(o['long'], 'obj long') + '~') if 'long' in o else '\n'.join(lines[l0:l1 + 1])
    act = '\n'.join(lines[c0:c1 + 1])
    rest = '\n'.join(lines[c1 + 1:])
    if 'extras' in o:
        rest = re.sub(r'(?ms)^E\n[^\n]*~\n.*?^~\n?', '', rest)
        ex = ''.join('E\n%s~\n%s\n~\n' % (kw, zb.wrap_plain(tilde(t, 'extra'))) for kw, t in o['extras'].items())
        # E blocks go after the 3 value lines, before any A blocks
        rl = rest.split('\n')
        rest = '\n'.join(rl[:3]) + '\n' + ex + '\n'.join(rl[3:])
        rest = rest.replace('\n\n', '\n')
    return '\n'.join([lines[0], al, sh, lo, act]) + '\n' + rest


def new_mob_text(m):
    st = zb.mob_stats(m.get('role', 'standard'), m['level'])
    flags = 'd' + m.get('flags', '')
    aff = m.get('aff', '') or '0'
    t = ('#%d\n%s~\n%s~\n%s\n~\n%s\n~\n%s %s %d E\n%d %d %d %dd%d+%d %dd%d+%d\n%d %d\n%d %d %d\n'
         % (m['vnum'], m['aliases'], m['short'], m['long'].rstrip(), zb.wrap_plain(m['desc']),
            flags, aff, m.get('align', 0), st['level'], st['thac0'], st['ac'], *st['hp'], *st['dam'],
            m.get('gold', st['gold']), st['exp'], 8, 8, m.get('sex', 0)))
    t += 'BareHandAttack: %d\nE\n' % zb.ATTACKS[m.get('attack', 'hit')]
    return t


def new_obj_text(o):
    kind, lvl = o['kind'], o.get('level', 1)
    wear, vals = 1, [0, 0, 0, 0]
    if kind == 'weapon':
        n, s = o.get('dice') or zb.weapon_dice(lvl, o.get('two_handed', False))
        vals = [0, n, s, zb.ATTACKS[o.get('attack', 'slash')]]
        wear |= zb.WEAR_BITS['wield']
    elif kind == 'armor':
        vals = [o.get('ac', zb.armor_value(lvl, o['slot'])), 0, 0, 0]
        wear |= zb.WEAR_BITS[o['slot']]
    elif kind == 'worn':
        wear |= zb.WEAR_BITS[o['slot']]
    elif kind == 'light':
        vals = [0, 0, o.get('hours', -1), 0]
        wear |= zb.WEAR_BITS['hold']
    elif kind == 'food':
        vals = [o.get('hours', 8), 0, 0, 0]
    elif kind == 'potion':
        sp = [x if x else -1 for x in o.get('spells', [])] + [-1, -1, -1]
        vals = [o.get('spell_level', lvl), sp[0], sp[1], sp[2]]
    elif kind == 'drinkcon':
        vals = [o.get('capacity', 10), o.get('capacity', 10), o.get('liquid', 0), 0]
        wear |= zb.WEAR_BITS['hold']
    if o.get('fixed'):
        wear = 0
    weight = o.get('weight', {'weapon': 8, 'armor': 10}.get(kind, 2))
    cost = o.get('cost', int(10 + lvl ** 1.7))
    t = ('#%d\n%s~\n%s~\n%s~\n~\n%d %s %d\n%d %d %d %d\n%d %d %d\n'
         % (o['vnum'], o['aliases'], o['short'], o['long'], zb.ITEM_TYPES[kind], o.get('extra', '0') or '0',
            wear, *vals, weight, cost, max(1, cost // 10)))
    for kw, text in o.get('extras', {}).items():
        t += 'E\n%s~\n%s\n~\n' % (kw, zb.wrap_plain(text))
    for loc, mod in o.get('affects', []):
        t += 'A\n%d %d\n' % (zb.APPLY[loc], mod)
    return t


def rewrite(ext, edits, fn, new=()):
    """Apply fn to each block named in edits, per file; append new blocks."""
    byfile = {}
    where = {}
    d = os.path.join(WORLD, ext)
    for f in os.listdir(d):
        if f.endswith('.' + ext):
            for m in re.finditer(r'(?m)^#(\d+)\s*$', open(os.path.join(d, f)).read()):
                where[int(m.group(1))] = int(f.split('.')[0])
    for v, e in edits.items():
        if v not in where:
            raise zb.SpecError('%s %d does not exist' % (ext, v))
        byfile.setdefault(where[v], {})[v] = e
    for n in new:
        byfile.setdefault(n['zone'], {})
    out = {}
    for z, ed in byfile.items():
        path = os.path.join(WORLD, ext, '%d.%s' % (z, ext))
        text = open(path).read()
        head, bl = blocks(text)
        seen = set()
        for b in bl:
            if b[0] in ed:
                last = b[1].rstrip('\n').endswith('$')
                body = b[1]
                if last:
                    body = re.sub(r'\$\s*$', '', body)
                b[1] = fn(body, ed[b[0]], b[0])
                if not b[1].endswith('\n'):
                    b[1] += '\n'
                if last:
                    b[1] += '$\n'
                seen.add(b[0])
        missing = set(ed) - seen
        if missing:
            raise zb.SpecError('%s/%d: no such vnums %s' % (ext, z, sorted(missing)))
        adds = [n for n in new if n['zone'] == z]
        if adds:
            addv = {n['vnum'] for n in adds}
            bl = [b for b in bl if b[0] not in addv]      # re-run: replace our own earlier copy
            gen = new_mob_text if ext == 'mob' else new_obj_text
            # insert in vnum order, keeping the file's final '$'
            bl = [[v, re.sub(r'\$\s*$', '', s)] for v, s in bl]
            bl += [[n['vnum'], gen(n)] for n in adds]
            bl.sort(key=lambda x: x[0])
            bl[-1][1] = bl[-1][1].rstrip('\n') + '\n$\n'
            if not bl:
                pass
        if not bl and adds:
            pass
        out[path] = head + ''.join(s for _, s in bl)
    return out


def redo_zone(z, name, add, remove):
    path = os.path.join(WORLD, 'zon', '%d.zon' % z)
    lines = open(path).read().rstrip('\n').split('\n')
    if name:
        lines[2] = tilde(name, 'zone name') + '~'
    # resets this tool added earlier carry a '*rt' tag; drop them so re-runs don't duplicate
    lines = [l for l in lines if not l.endswith('\t*rt')]
    add = [a + '\t*rt' for a in add]
    if remove:
        lines = [l for l in lines if not any(l.startswith(p) for p in remove)]
    if add:
        si = max(i for i, l in enumerate(lines) if l.strip() == 'S')
        lines = lines[:si] + add + lines[si:]
    return {path: '\n'.join(lines) + '\n'}


def main(argv):
    check = '--check' in argv
    args = [a for a in argv if not a.startswith('--')]
    path = args[0]
    if not os.path.exists(path):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'retheme', path + '.py')
    spec = importlib.util.spec_from_file_location('rt', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    R = mod.RETHEME
    files = {}
    files.update(rewrite('wld', R.get('rooms', {}), redo_room))
    files.update(rewrite('mob', R.get('mobs', {}), redo_mob, R.get('new_mobs', [])))
    files.update(rewrite('obj', R.get('objs', {}), redo_obj, R.get('new_objs', [])))
    zs = set(R.get('zones', {})) | set(R.get('resets', {})) | set(R.get('remove_resets', {}))
    for z in zs:
        files.update(redo_zone(z, R.get('zones', {}).get(z), R.get('resets', {}).get(z, []),
                               R.get('remove_resets', {}).get(z, [])))
    for p, t in sorted(files.items()):
        print(('check ' if check else 'write ') + os.path.relpath(p, WORLD))
        if not check:
            with open(p, 'w') as fh:
                fh.write(t)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except zb.SpecError as e:
        print('error:', e)
        sys.exit(1)
