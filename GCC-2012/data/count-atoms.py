#!/usr/bin/env python

from collections import Counter
import sys

stats = dict()
commit_counter = 0
lock = False
for line in open(sys.argv[1]):
    line = line.strip()
    if not line:
        continue

    if line.startswith('Author') or line.startswith('Update from') or line.startswith('commit'):
        continue

    if line.startswith('Date'):
        date_line = line
        stats[ commit_counter ] = [line,Counter()]
        continue
    if line.startswith('---') and line == '--- /dev/null':
        # not a changed file, its a new file, exclude from stats
        lock = True

    if line.startswith('---') and not line == '--- /dev/null':
        # not a changed file, its a new file, exclude from stats
        lock = False

    if not lock and line.startswith('+') or line.startswith('-'):
        stats[ commit_counter ][1].update( [line.split()[0]] )




hetatm_m = 0
hetatm_p = 0

compound_m = 0
compound_p = 0

atom_m = 0
atom_p = 0

for k in sorted(stats.keys(), reverse=True):
    if stats[k][0].find(sys.argv[2].split()[0]) != -1 and stats[k][0].find(sys.argv[2].split()[-1]) != -1:
        hetatm_m += stats[k][1]['-HETATM']
        hetatm_p += stats[k][1]['+HETATM']
        compound_p += stats[k][1]['+COMPND']
        compound_m += stats[k][1]['-COMPND']
        atom_m += stats[k][1]['-ATOM']
        atom_p += stats[k][1]['+ATOM']
print hetatm_m, hetatm_p
print compound_m, compound_p
print atom_m, atom_p
