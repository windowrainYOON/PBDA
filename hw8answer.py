#!/usr/bin/env python3

import sys

ksize = int(sys.argv[1])
fpath = sys.argv[2]

myseq = open(fpath).read().rstrip()

mydic = {}
for i in range(0, len(myseq)-ksize+1):
  kmer = myseq[i:i+ksize]
  if mydic.get(kmer, -1) == -1 :
    mydic[kmer] = 1
  else:
    mydic[kmer] += 1

mylist = sorted(list(mydic.values()))
maxcnt = mylist[-1]

for cnt in range(1, maxcnt+1):
  cntnum = mylist.count(cnt)
  outstr = '%*d ' %(len(str(maxcnt)), cnt)
  outstr += chr(0x258c) * cntnum

  if cntnum > 0:
    outstr += ' (' + str(cntnum) + ')'
  
  print(outstr)
