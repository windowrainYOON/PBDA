#!/usr/bin/env python3

import sys

pfile = sys.argv[1]
fpath = sys.argv[2]

seq = ''
for line in open(fpath):
    if line[0] == '>':
        continue
    else:
        seq += line.upper().rstrip()


mypattern = []
for line in open(pfile):
    mylist = line.split()
    mydic = {}
    for (i, nt) in enumerate('ACGT'):
        mydic[nt] = float(mylist[i])
    mypattern.append(mydic)

max_score = 0
max_seq = ''
for i in range(0, len(seq) - len(mypattern) + 1):
    score = 1
    for j in range(0, len(mypattern)):
        score *= mypattern[j][seq[i+j]]
    if score >= max_score:
        max_score = score
        max_seq = seq[i:i+len(mypattern)]

print(max_score, max_seq)