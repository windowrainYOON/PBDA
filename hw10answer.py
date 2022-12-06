#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

myseq = ''
cnts = []
for line in open(fpath):
  tokens = line.split()

  if len(tokens) == 1:
    myseq += line.rstrip()
  else:
    if len(cnts) == 0: cnts = [0] * len(myseq)

    for pos in range(int(tokens[1]), int(tokens[2])+1):
      cnts[pos-1] += 1

mposLen = len(str(len(myseq)))
mcntLen = len(str(max(cnts)))

pi, pcnt = -1, -1
for i in range(0, len(cnts)):
  cnt = cnts[i]

  if pi != -1 and cnt != pcnt:
    print('%*d - %*d : %*d %s' %(mposLen, pi+1, mposLen, i, mcntLen, pcnt, chr(0x258c)*pcnt))
    pi = i

  if i == 0: pi = i

  pcnt = cnt

print('%*d - %*d : %*d %s' %(mposLen, pi+1, mposLen, len(cnts), mcntLen, pcnt, chr(0x258c)*pcnt))