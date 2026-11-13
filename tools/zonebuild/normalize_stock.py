"""Soften stock (non-zonebuild) mobs to the zonebuild scaling formula.

Stock zones were re-levelled by relevel.py but kept stock CircleMUD accuracy, armour
and damage, so they were much harder than zonebuild mobs of the same level.  The
user chose the zonebuild formula as the standard (2026-11-13).

For each mob in a zone whose .zon builder line is not 'Claude~' (immortal zones
0/12/13 and shopkeeper-type mobs with hp bonus >= 5000 are skipped):
  * role = the zonebuild role whose formula HP is closest to the mob's HP
  * thac0 and AC are raised to the formula value if the stock value is tougher
  * damage per hit (wielded weapon dice, else bare dice, plus damroll) is capped at
    the formula value; mobs that wield a weapon are capped through damroll only
Nothing is ever made harder.  Re-running is a no-op.

usage: normalize_stock.py [--check] [zone ...]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zonebuild as zb

W = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib/world')
SKIP_ZONES = {0, 12, 13}
ROLES = ('standard', 'elite', 'champion', 'boss')
STAT = re.compile(r'(?m)^(-?\d+) (-?\d+) (-?\d+) (\d+)d(\d+)\+(-?\d+) (\d+)d(\d+)\+(-?\d+)$')


def weapons():
    out = {}
    for f in os.listdir(W + '/obj'):
        if not f.endswith('.obj'):
            continue
        for b in re.split(r'(?m)^(?=#\d+\s*$)', open(W + '/obj/' + f).read())[1:]:
            L = b.split('\n'); i = 3
            while not L[i].endswith('~'): i += 1
            i += 1
            while not L[i].endswith('~'): i += 1
            i += 1
            if L[i].split()[0] == '5':
                v = L[i + 1].split()
                out[int(L[0][1:])] = int(v[1]) * (int(v[2]) + 1) / 2
    return out


def wielders(wpn):
    out = {}
    for f in os.listdir(W + '/zon'):
        if not f.endswith('.zon'):
            continue
        last = None
        for l in open(W + '/zon/' + f):
            p = l.split()
            if p and p[0] == 'M':
                last = int(p[2])
            elif p and p[0] == 'E' and len(p) > 4 and p[4] == '16' and int(p[2]) in wpn:
                out[last] = max(out.get(last, 0), wpn[int(p[2])])
    return out


def formula(level, hp):
    best = None
    for r in ROLES:
        st = zb.mob_stats(r, max(1, level - zb.ROLE[r][3]))
        h = st['hp'][0] * (st['hp'][1] + 1) / 2 + st['hp'][2]
        d = abs(hp - h) / h
        if best is None or d < best[0]:
            best = (d, r, st)
    return best[1], best[2]


def main():
    check = '--check' in sys.argv
    only = {int(a) for a in sys.argv[1:] if a.isdigit()}
    wield = wielders(weapons())
    total = 0
    for f in sorted(os.listdir(W + '/zon'), key=lambda x: int(x.split('.')[0]) if x[0].isdigit() else -1):
        if not f.endswith('.zon'):
            continue
        z = int(f[:-4])
        if z in SKIP_ZONES or (only and z not in only):
            continue
        if open(W + '/zon/' + f).read().split('\n')[1].strip() == 'Claude~':
            continue
        path = '%s/mob/%d.mob' % (W, z)
        if not os.path.exists(path):
            continue
        text = open(path).read()
        out = []; changed = 0
        for b in re.split(r'(?m)^(?=#\d+\s*$)', text):
            m = re.match(r'#(\d+)', b)
            s = STAT.search(b) if m else None
            if not s:
                out.append(b); continue
            v = int(m.group(1))
            lv, th, ac, hn, hs, hb, dn, ds, db = map(int, s.groups())
            hp = hn * (hs + 1) / 2 + hb
            if hb >= 5000 or lv < 1:
                out.append(b); continue
            role, st = formula(lv, hp)
            fdn, fds, fdb = st['dam']
            fdph = fdn * (fds + 1) / 2 + fdb
            nth, nac = max(th, st['thac0']), max(ac, st['ac'])
            ndn, nds, ndb = dn, ds, db
            if v in wield:
                if wield[v] + db > fdph + 0.5:
                    ndb = max(0, round(fdph - wield[v]))
            elif dn * (ds + 1) / 2 + db > fdph + 0.5:
                ndn, nds, ndb = fdn, fds, fdb
            new = '%d %d %d %dd%d+%d %dd%d+%d' % (lv, nth, nac, hn, hs, hb, ndn, nds, ndb)
            if new != s.group(0):
                changed += 1
                print('  %5d %-30s %-8s %s -> %s' % (v, b.split('\n')[2].rstrip('~')[:30], role, s.group(0), new))
                b = b[:s.start()] + new + b[s.end():]
            out.append(b)
        if changed:
            print('zone %d: %d mobs softened' % (z, changed))
            total += changed
            if not check:
                open(path, 'w').write(''.join(out))
    print('%s %d mobs' % ('would change' if check else 'changed', total))


if __name__ == '__main__':
    main()
