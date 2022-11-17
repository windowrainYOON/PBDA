#!/usr/bin/env python3

import sys

fpath = sys.argv[1]
myseq = open(fpath).read().rstrip()

dt_cnt = {}

for x in 'ACCGT':
  for y in 'ACGT':
    dt_cnt[x+y] = 0

for i in range(0, len(myseq)):
  nt1 = myseq[i]
  nt2 = myseq[-1*i -1]
  dt_cnt[nt1+nt2] += 1

numlist = []
for x in 'ACGT':
  for y in 'ACGT':
    cnt = dt_cnt[x+y]
    numlist.append(cnt)

numlist.sort()
_min, _max = numlist[0], numlist[-1]
cw = len(str(_max))

print('\tA\tC\tG\tT')
for x in 'ACCGT':
  out_str = '%s\t%0*d\t%0*d\t%0*d\t%0*d' %(x, cw, dt_cnt[x+'A'], cw, dt_cnt[x+'C'], cw, dt_cnt[x+'G'], cw, dt_cnt[x+'T'])
  print(out_str)