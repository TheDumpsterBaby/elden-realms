#!/usr/bin/env python3
"""Cap exp and gold of mobs in the older zones to the new reward curve.

zonebuild.py pays exp = x * 12 * L^2 + 10 and gold = L^1.6 * (1 + x/5), where x
is the role multiplier (standard 1, elite 3, champion 10, boss 30).  Stock mobs
have no role, so one is inferred from toughness: rounds = avg hp / (0.7L + 5),
i.e. how many rounds a lone player of the mob's level needs to kill it
(standard 10, elite 25, champion 87.5, boss 200), interpolated on a log scale.
Gold above GOLD_SLACK x its curve gold is cut to that limit.

Exp is NOT held to zonebuild's 12*L^2 curve: the stock exp table charges ~375k
a level through 10-20, where that curve would mean 100-200 kills a level, so
the old zones' higher exp is what keeps that band playable.  Instead exp is
capped against the exp table itself: a kill may pay at most
EXP_SHARE x role multiplier of the exp needed for the mob's level (a standard
mob <= 6% of a level).  That trims only the wild outliers.  Nothing is ever raised; re-running is a no-op.
Shopkeepers (hp bonus >= 5000) are left alone.
Usage: rewardfix.py [--check] [-v]
"""
import math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zonebuild as zb  # noqa: E402

WORLD = zb.WORLD
NEW = {50, 60, 61, 62, 63} | set(range(200, 215))
SKIP = {0, 12, 13} | NEW
EXP_SHARE, GOLD_SLACK = 0.06, 2.0
PTS = [(10, 1), (25, 3), (87.5, 10), (200, 30)]
STAT = re.compile(r'^(-?\d+) (-?\d+) (-?\d+) (\d+)d(\d+)\+(-?\d+) ')


def exp_table():
    """mean over classes of exp needed to go from level L to L+1"""
    src = open(os.path.join(zb.WORLD, '..', '..', 'src', 'class.c')).read()
    body = src[src.index('exp_table[NUM_CLASSES]'):]
    body = body[:body.index('};')]
    rows = [list(map(int, re.findall(r'\d+', blk))) for blk in re.split(r'\{\s*/\*[^*]*\*/', body)[1:]]
    n = min(len(r) for r in rows)
    return [sum(r[i + 1] - r[i] for r in rows) / len(rows) for i in range(n - 1)]


def role_x(rounds):
    r = max(rounds, 1)
    if r <= PTS[0][0]:
        return max(0.2, PTS[0][1] * r / PTS[0][0])
    for (r0, x0), (r1, x1) in zip(PTS, PTS[1:]):
        if r <= r1:
            t = (math.log(r) - math.log(r0)) / (math.log(r1) - math.log(r0))
            return math.exp(math.log(x0) + t * (math.log(x1) - math.log(x0)))
    return PTS[-1][1]


def main(check, verbose):
    total = 0
    delta = exp_table()
    for f in sorted(os.listdir(os.path.join(WORLD, 'mob')), key=lambda s: int(s.split('.')[0]) if s[0].isdigit() else -1):
        if not f.endswith('.mob') or int(f[:-4]) in SKIP:
            continue
        path = os.path.join(WORLD, 'mob', f)
        text = open(path).read()
        parts = re.split(r'(?m)^(?=#\d+\s*$)', text)
        n = 0
        for k, b in enumerate(parts[1:], 1):
            L, t, i = b.split('\n'), 0, 1
            while t < 4:
                t += L[i].endswith('~')
                i += 1
            m = STAT.match(L[i + 1])
            lv, hn, hs, hb = int(m.group(1)), int(m.group(4)), int(m.group(5)), int(m.group(6))
            if hb >= 5000:
                continue
            lv = max(1, lv)
            x = role_x((hn * (hs + 1) / 2 + hb) / (0.7 * lv + 5))
            g = L[i + 2].split()
            gold, exp = int(g[0]), int(g[1])
            emax = int(EXP_SHARE * x * delta[min(lv, len(delta) - 1)])
            gmax = int(GOLD_SLACK * (lv ** 1.6) * (1 + x / 5))
            ne, ng = min(exp, emax), min(gold, gmax)
            if (ne, ng) != (exp, gold):
                n += 1
                if verbose:
                    print('  %s L%d x%.1f: exp %d -> %d, gold %d -> %d' % (L[2].rstrip('~'), lv, x, exp, ne, gold, ng))
                g[0], g[1] = str(ng), str(ne)
                L[i + 2] = ' '.join(g)
                parts[k] = '\n'.join(L)
        if n:
            print('%s zone %s: %d mobs capped' % ('check' if check else 'fixed', f[:-4], n))
            total += n
            if not check:
                open(path, 'w').write(''.join(parts))
    print('%d mobs changed' % total)


if __name__ == '__main__':
    main('--check' in sys.argv, '-v' in sys.argv)
