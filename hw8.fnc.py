#!/usr/bin/env python3

import sys
kcount = int(sys.argv[1])
seq = open(sys.argv[2]).read().rstrip()

def filterKmerAsDic(seqDic, kmer):
  if seqDic.get(kmer, -1) == -1:
    seqDic[kmer] = 1
  else:
    seqDic[kmer] += 1
  
  return seqDic

def countKmerFromSeq(kcount, seq):
  seqDic = {}

  for i in range(len(seq)-kcount):
    kmer = ''
    for j in range(kcount):
      kmer += seq[i+j]
    seqDic = filterKmerAsDic(seqDic, kmer)
  
  return seqDic

def alignDicAsResult(seqDic):
  seqCountType = list(set(list(seqDic.values())))
  seqCountType.sort()
  _format = len(str(max(seqCountType)))

  seqCountDic ={x:0 for x in range(1, max(seqCountType)+1)}

  for i in seqDic:
    seqCountDic[seqDic[i]] += 1
  
  return seqCountDic, _format


seqDic = countKmerFromSeq(kcount, seq)
seqCountDic, _format = alignDicAsResult(seqDic)

for i in seqCountDic:
  bars = chr(0x258C)*seqCountDic[i]
  numbers = ''
  if seqCountDic[i] != 0:
    numbers = '(%s)' %(str(seqCountDic[i]))
  print('%*d %s %s' %(_format, i, bars, numbers))