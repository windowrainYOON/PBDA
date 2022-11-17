#!/usr/bin/env python3

import sys
kcount = int(sys.argv[1])
seq = open(sys.argv[2]).read().rstrip()
seqDic = {}

for i in range(len(seq)-kcount):
  kmer = ''
  for j in range(kcount):
    kmer += seq[i+j]
  if seqDic.get(kmer, -1) == -1:
    seqDic[kmer] = 1
  else:
    seqDic[kmer] += 1

seqCountType = list(set(list(seqDic.values())))
seqCountType.sort()

seqCountDic ={x:0 for x in range(1, max(seqCountType)+1)}

for i in seqDic:
  seqCountDic[seqDic[i]] += 1

for i in seqCountDic:
  bars = chr(0x258C)*seqCountDic[i]
  numbers = ''
  if seqCountDic[i] != 0:
    numbers = '(%s)' %(str(seqCountDic[i]))
  print('%*d %s %s' %(len(str(max(seqCountType))), i, bars, numbers))