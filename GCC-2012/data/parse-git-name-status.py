#!/usr/bin/env python

from collections import Counter
import sys

stats = dict()
commit_counter = 0
for line in open(sys.argv[1]):
    line = line.strip()
    if not line:
        continue
        
    if line.startswith('commit'):
        iid = line.split()[-1]
        commit_counter += 1
        stats[ commit_counter ] = ['',Counter()]
        continue

    if line.startswith('Author') or line.startswith('Update from'):
        continue

    if line.startswith('Date'):
        stats[ commit_counter ][0] = line
        continue
    stats[commit_counter][1].update( line.split()[0] )


a = 0
m = 0
for k in sorted(stats.keys(), reverse=True):
    print stats[k]
    if stats[k][0].find(sys.argv[2].split()[0]) != -1 and stats[k][0].find(sys.argv[2].split()[-1]) != -1:
        
        a += stats[k][1]['A']
        m += stats[k][1]['M']
print a
print m
