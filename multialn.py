#!/usr/bin/env python3

import sys

fpath = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])
indel = int(sys.argv[4])

def pair_score (seqA, seqB):
    score = 0
    for i in range(0, len(seqA)):
        ntA = seqA[i]
        ntB = seqB[i]

        if ntA == '-' and ntB == '-': continue

        if ntA == ntB:
            score += match
        elif ntA == '-' or ntB == '-':
            score += indel
        else:
            score += mismatch
    return score

lines = ''
for line in open(fpath):
    if line[0] == '>':
        lines += line.rstrip() + '>'
    else:
        lines += line.rstrip()

mysum = 0
mycnt = 0
mylist = lines.split('>')
for i in range(2, len(mylist)-2, 2):
    seqA = mylist[i]
    for j in range(i+2, len(mylist), 2):
        seqB = mylist[i]

        mysum += pair_score(seqA, seqB)
        mycnt += 1

print(mysum/mycnt)