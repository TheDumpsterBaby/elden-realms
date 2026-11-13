#!/usr/bin/env python3
"""Bring stock gear in the older zones down to the new item curve.

The new zones (zonebuild.py) give a level-L weapon about 2.5 + 0.11*L average
damage, armour armor_value(L, slot), and a small affect budget.  Stock items in
the re-levelled eastern zones (10-30) were often far above that, which made a
level-25 drop better than W4-W6 gear.  For every object outside the new zones
this tool works out the level it loads at (the highest-level mob that carries
it, else the zone's median mob level) and caps it at that level + SLACK:

  * weapon dice   -> weapon_dice(L + SLACK), +1.5 avg for two-handers
  * armour value  -> armor_value(L + SLACK, slot)
  * affects       -> positive affects scaled down so the budget score is at
                     most 3 + L/8 (negatives -- curses, trade-offs -- kept)

Only items above the cap are touched, so re-running is a no-op.  Shop stock is
capped the same way (by the shopkeeper's zone level, not the keeper's).
Usage: gearfix.py [--check]
"""
import os, re, statistics, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zonebuild as zb  # noqa: E402

WORLD = zb.WORLD
SLACK = 10
NEW = {50, 60, 61, 62, 63} | set(range(200, 215))
SKIP = {0, 12, 13} | NEW          # immortal zones, and the new zones (already on curve)
SLOTS = [(2, 'finger'), (4, 'neck'), (8, 'body'), (16, 'head'), (32, 'legs'), (64, 'feet'), (128, 'hands'),
         (256, 'arms'), (512, 'shield'), (1024, 'about'), (2048, 'waist'), (4096, 'wrist')]
BASE = {'body': 10, 'shield': 8, 'head': 6, 'legs': 6, 'arms': 5, 'about': 5,
        'hands': 4, 'feet': 4, 'waist': 3, 'wrist': 2, 'neck': 2, 'finger': 1}
TWO_HANDED = re.compile(r'two-handed|halberd|bardiche|awl-pike|pike|greatsword|maul|huge spiked club|bastard', re.I)
WEIGHT = {18: 1, 19: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 13: .1, 12: 1 / 15, 14: .04}   # per point of mod
NEG = {17: -1 / 3, 20: -.5, 21: -.5, 22: -.5, 23: -.5, 24: -.5}                           # lower is better


def zones():
    zr = {}
    for f in os.listdir(os.path.join(WORLD, 'zon')):
        if f.endswith('.zon'):
            L = open(os.path.join(WORLD, 'zon', f)).read().split('\n')
            lo, hi = map(int, L[3].split()[:2])
            zr[int(f[:-4])] = (lo, hi, L)
    return zr


def zone_of(zr, v):
    for z, (lo, hi, _) in zr.items():
        if lo <= v <= hi:
            return z


def mob_levels():
    out = {}
    for f in os.listdir(os.path.join(WORLD, 'mob')):
        if not f.endswith('.mob'):
            continue
        for b in re.split(r'(?m)^(?=#\d+\s*$)', open(os.path.join(WORLD, 'mob', f)).read())[1:]:
            v = int(re.match(r'#(\d+)', b).group(1))
            L, n, i = b.split('\n'), 0, 1
            while n < 4:
                n += L[i].endswith('~')
                i += 1
            s = L[i + 1].split()
            out[v] = (int(s[0]), int(re.match(r'\d+d\d+\+(-?\d+)', s[3]).group(1)))
    return out


def load_levels(zr, mobs):
    """object vnum -> level it loads at"""
    zmed = {}
    for v, (lv, hpb) in mobs.items():
        if hpb < 5000:
            zmed.setdefault(zone_of(zr, v), []).append(lv)
    zmed = {z: int(statistics.median(l)) for z, l in zmed.items()}
    carried = {}
    for z, (_, _, L) in zr.items():
        last = None
        for l in L:
            p = l.split()
            if len(p) > 3 and p[0] == 'M':
                last = int(p[2])
            elif len(p) > 3 and p[0] in 'EG' and last in mobs and mobs[last][1] < 5000:
                carried.setdefault(int(p[2]), []).append(mobs[last][0])
    return lambda o, z: max(carried[o]) if o in carried else zmed.get(z, 1)


def score(aff):
    s = 0.0
    for loc, m in aff:
        if loc in NEG:
            s += m * NEG[loc]
        else:
            s += m * WEIGHT.get(loc, 0)
    return s


def fix_block(b, L, notes, v):
    lines = b.split('\n')
    i = 3
    while not lines[i].endswith('~'):
        i += 1
    i += 1
    while not lines[i].endswith('~'):
        i += 1
    i += 1
    tl, vl = lines[i].split(), lines[i + 1].split()
    typ, name = int(tl[0]), lines[2].rstrip('~')
    try:
        wear = int(tl[2])
    except ValueError:
        wear = sum(1 << (ord(c) - 97) for c in tl[2] if c.islower())
    cap = L + SLACK
    if typ == 5:
        n, s = int(vl[1]), int(vl[2])
        two = bool(TWO_HANDED.search(name))
        avg_cap = 2.5 + cap * 0.11 + (1.5 if two else 0)
        if n * (s + 1) / 2 > avg_cap + 0.75:
            nn, ns = zb.weapon_dice(cap, two)
            notes.append('%d %s: weapon %dd%d -> %dd%d' % (v, name, n, s, nn, ns))
            vl[1], vl[2] = str(nn), str(ns)
    if typ == 9:
        slot = next((nm for bit, nm in SLOTS if wear & bit), None)
        if slot:
            ac, mx = int(vl[0]), zb.armor_value(cap, slot)
            if ac > mx:
                notes.append('%d %s: armour %d -> %d (%s)' % (v, name, ac, mx, slot))
                vl[0] = str(mx)
    lines[i + 1] = ' '.join(vl)
    # affects
    aidx = [k for k in range(i + 3, len(lines) - 1) if lines[k] == 'A']
    aff = [tuple(map(int, lines[k + 1].split()[:2])) for k in aidx]
    budget = 3 + L / 8
    sc = score(aff)
    if sc > budget + 0.01:
        pos = [(k, loc, m) for k, (loc, m) in zip(aidx, aff) if (m * NEG[loc] if loc in NEG else m * WEIGHT.get(loc, 0)) > 0]
        neg = sc - sum((m * NEG[loc] if loc in NEG else m * WEIGHT.get(loc, 0)) for _, loc, m in pos)
        possc = sc - neg
        f = max(0.0, (budget - neg) / possc) if possc else 1
        new = []
        for k, loc, m in pos:
            nm = int(m * f) if m > 0 else -int(-m * f)
            if nm == 0:
                nm = 1 if m > 0 else -1
            lines[k + 1] = '%d %d' % (loc, nm)
            new.append('%d:%d->%d' % (loc, m, nm))
        notes.append('%d %s: affects %.1f > %.1f, %s' % (v, name, sc, budget, ' '.join(new)))
    return '\n'.join(lines)


def main(check):
    zr, mobs = zones(), mob_levels()
    lvl = load_levels(zr, mobs)
    notes = []
    for f in sorted(os.listdir(os.path.join(WORLD, 'obj'))):
        if not f.endswith('.obj') or int(f[:-4]) in SKIP:
            continue
        path = os.path.join(WORLD, 'obj', f)
        text = open(path).read()
        parts = re.split(r'(?m)^(?=#\d+\s*$)', text)
        out = [parts[0]]
        for b in parts[1:]:
            v = int(re.match(r'#(\d+)', b).group(1))
            out.append(fix_block(b, lvl(v, zone_of(zr, v)), notes, v))
        new = ''.join(out)
        if new != text and not check:
            open(path, 'w').write(new)
    for n in notes:
        print(('check ' if check else 'fixed ') + n)
    print('%d changes' % len(notes))


if __name__ == '__main__':
    main('--check' in sys.argv)
