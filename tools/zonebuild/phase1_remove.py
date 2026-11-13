#!/usr/bin/env python3
"""
Phase 1 of the World Zone Plan: remove the nine zones west of Midgaard and the
four out-of-theme zones, and every reference to them.

  - deletes their .wld/.mob/.obj/.zon/.shp files and index entries
  - removes exits in kept rooms that lead into them
  - removes spec_assign.c lines that attach procedures to their mob vnums
    (those vnums are reused by new zones)

Idempotent: running it twice changes nothing the second time.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORLD = os.path.join(ROOT, 'lib', 'world')
REMOVED = {9: 'River Island of Minos', 36: 'Chessboard', 50: 'Great Eastern Desert',
           53: 'Great Pyramid', 60: 'Haon-Dor Light', 61: 'Haon-Dor Dark', 62: 'Orc Enclave',
           63: 'Arachnos', 120: 'Rome'}
RANGES = [(z * 100, z * 100 + 99) for z in REMOVED]


def rebuilt(z):
    """A zone number reused by a zonebuild zone (its .zon names Claude as builder)."""
    p = os.path.join(WORLD, 'zon', '%d.zon' % z)
    return os.path.exists(p) and open(p, encoding='latin-1').read().split('\n')[1].strip() == 'Claude~'


def existing_rooms():
    rooms = set()
    wdir = os.path.join(WORLD, 'wld')
    for f in os.listdir(wdir):
        if f.endswith('.wld'):
            rooms |= {int(v) for v in re.findall(r'^#(\d+)$', open(os.path.join(wdir, f), encoding='latin-1').read(), re.M)}
    return rooms


def removed(v):
    return any(a <= v <= b for a, b in RANGES)


def drop_files():
    for z in [z for z in REMOVED if rebuilt(z)]:
        del REMOVED[z]                      # a new zone lives in this slot now: keep it
    for ext in ('wld', 'mob', 'obj', 'zon', 'shp'):
        idx = os.path.join(WORLD, ext, 'index')
        if not os.path.exists(idx):
            continue
        lines = [l.strip() for l in open(idx) if l.strip()]
        keep = [l for l in lines if not (re.match(r'(\d+)\.', l) and int(l.split('.')[0]) in REMOVED)]
        if keep != lines:
            open(idx, 'w').write('\n'.join(keep) + '\n')
        for z in REMOVED:
            p = os.path.join(WORLD, ext, '%d.%s' % (z, ext))
            if os.path.exists(p):
                os.remove(p)
                print('deleted', os.path.relpath(p, ROOT))


def drop_exits():
    wdir = os.path.join(WORLD, 'wld')
    for f in sorted(os.listdir(wdir)):
        if not f.endswith('.wld'):
            continue
        path = os.path.join(wdir, f)
        text = open(path, encoding='latin-1').read()
        # an exit block: D<n>\n<desc lines>~\n<keywords>~\n<info> <key> <to>\n
        pat = re.compile(r'^D\d[ \t]*\n(?:[^\n]*\n)*?[^\n]*~\n[^\n]*~\n-?\d+ -?\d+ (-?\d+)\n', re.M)
        out, pos, n = [], 0, 0
        for m in pat.finditer(text):
            if removed(int(m.group(1))) and int(m.group(1)) not in ROOMS:
                out.append(text[pos:m.start()]); pos = m.end(); n += 1
        if n:
            out.append(text[pos:])
            open(path, 'w', encoding='latin-1').write(''.join(out))
            print('%s: removed %d exit(s) into removed zones' % (f, n))


def drop_spec_assign():
    path = os.path.join(ROOT, 'src', 'spec_assign.c')
    lines = open(path).read().split('\n')
    keep = []
    for l in lines:
        m = re.match(r'\s*ASSIGN(MOB|OBJ|ROOM)\((\d+),', l)
        if m and removed(int(m.group(2))) and (int(m.group(2)) // 100) in REMOVED:
            continue
        keep.append(l)
    if len(keep) != len(lines):
        open(path, 'w').write('\n'.join(keep))
        print('spec_assign.c: removed %d line(s)' % (len(lines) - len(keep)))


if __name__ == '__main__':
    drop_files()
    ROOMS = existing_rooms()
    drop_exits()
    drop_spec_assign()
