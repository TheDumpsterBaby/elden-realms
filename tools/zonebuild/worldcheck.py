#!/usr/bin/env python3
"""World sanity check: dead exits, one-way exits between zones, unreachable rooms."""
import re, glob, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
R = {}
for f in glob.glob(os.path.join(ROOT, 'lib/world/wld/*.wld')):
    t = open(f, encoding='latin-1').read()
    for blk in re.split(r'\n(?=#\d+\n)', '\n' + t):
        m = re.match(r'\s*#(\d+)\n(.*?)~', blk, re.S)
        if not m: continue
        R[int(m.group(1))] = (m.group(2).strip(), {'neswud'[int(d)]: int(to) for d, to in
                              re.findall(r'\nD(\d)[ \t]*\n(?:.*\n)*?.*~\n.*~\n-?\d+ -?\d+ (-?\d+)', blk)})
REV = dict(zip('neswud', 'swneud'[0:0] or 'swnedu'))
dead = [(v, d, t) for v, (n, ex) in R.items() for d, t in ex.items() if t != -1 and t not in R]
z = lambda v: v // 100
oneway = [(v, d, t) for v, (n, ex) in R.items() for d, t in ex.items()
          if t in R and z(t) != z(v) and R[t][1].get(REV[d]) != v]
seen, q = {3001}, collections.deque([3001])
while q:
    v = q.popleft()
    for t in R[v][1].values():
        if t in R and t not in seen: seen.add(t); q.append(t)
zones = sorted({z(v) for v in R})
unreach = {zz: sum(1 for v in R if z(v) == zz and v not in seen) for zz in zones}
print('rooms', len(R), '| dead exits', dead, '| one-way between zones', oneway)
print('unreachable from the Temple by zone:', {k: c for k, c in unreach.items() if c})
for v in [int(a) for a in sys.argv[1:]]:
    print(v, R[v][0], R[v][1])
