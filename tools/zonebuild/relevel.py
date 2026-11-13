#!/usr/bin/env python3
"""Re-level the older eastern zones into the 10-30 band (World Zone Plan).

Each zone's mobs are mapped linearly from their current level range onto a
band; hp, damage, thac0, ac, exp and gold scale with the new level so a mob
keeps its place in the zone's pecking order.  Shopkeepers and other
near-invulnerable town mobs (hp bonus >= 5000) are left alone.  Re-running is
a no-op: the second time, a zone's range already equals its band.
Usage: relevel.py [--check]
"""
import os, re, sys

WORLD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lib', 'world')
BANDS = {40: (10, 15), 35: (10, 15), 52: (12, 18), 33: (12, 20), 150: (14, 22), 64: (16, 22),
         79: (16, 24), 54: (15, 25), 51: (18, 26), 25: (18, 30), 65: (20, 28), 15: (24, 30)}
STAT = re.compile(r'^(-?\d+) (-?\d+) (-?\d+) (\d+)d(\d+)\+(-?\d+) (\d+)d(\d+)\+(-?\d+)\s*$')


def mobs(text):
    out = []
    for m in re.finditer(r'(?m)^#(\d+)\s*$', text):
        start = m.end() + 1
        lines, pos = [], start
        # walk: aliases~, short~, long..~, desc..~, flags line, stat line
        n_t = 0
        while n_t < 4:
            e = text.index('\n', pos)
            line = text[pos:e]
            if line.endswith('~'):
                n_t += 1
            pos = e + 1
        e = text.index('\n', pos); pos = e + 1             # flags line
        e = text.index('\n', pos)
        out.append((int(m.group(1)), pos, e))              # stat line span
        g = text.index('\n', e + 1)
        out[-1] += (e + 1, g)                               # gold/exp line span
    return out


def scale(L0, L1, k):
    return (L1 / max(1, L0)) ** k


def main(check):
    for z, (lo, hi) in sorted(BANDS.items()):
        path = os.path.join(WORLD, 'mob', '%d.mob' % z)
        text = open(path).read()
        rows = []
        for v, s, e, gs, ge in mobs(text):
            st = STAT.match(text[s:e])
            if not st:
                raise SystemExit('mob %d: cannot parse "%s"' % (v, text[s:e]))
            f = list(map(int, st.groups()))
            if f[5] >= 5000:
                continue
            rows.append((v, s, e, gs, ge, f))
        lv = [r[5][0] for r in rows]
        a, b = min(lv), max(lv)
        edits = []
        for v, s, e, gs, ge, f in rows:
            L0 = f[0]
            L1 = lo if a == b else round(lo + (L0 - a) * (hi - lo) / (b - a))
            if L1 == L0:
                continue
            hpk = (0.7 * L1 + 5) / (0.7 * max(1, L0) + 5)
            dk = scale(L0, L1, 1.0)
            thac0 = max(0, min(20, f[1] - (L1 - L0)))
            ac = max(-10, min(10, f[2] - (L1 - L0) // 3))
            hp_b = max(1, round(f[5] * hpk))
            dam_b = max(0, min(100, round(f[8] * dk)))
            stat = '%d %d %d %dd%d+%d %dd%d+%d' % (L1, thac0, ac, f[3], f[4], hp_b, f[6], f[7], dam_b)
            gold, exp = map(int, text[gs:ge].split()[:2])
            ge_line = '%d %d' % (round(gold * scale(L0, L1, 1.6)), round(exp * scale(L0, L1, 2)))
            edits.append((s, e, stat)); edits.append((gs, ge, ge_line))
            print('  %d: lvl %d -> %d' % (v, L0, L1))
        for s, e, new in sorted(edits, reverse=True):
            text = text[:s] + new + text[e:]
        print('zone %d: %d mobs, %d-%d -> %d-%d, %d changed' % (z, len(rows), a, b, lo, hi, len(edits) // 2))
        if not check:
            open(path, 'w').write(text)


if __name__ == '__main__':
    main('--check' in sys.argv)
