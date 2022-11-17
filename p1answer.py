#!/usr/bin/env python3

import sys
import random

fracA = float(sys.argv[1])
fracC = float(sys.argv[2])
fracG = float(sys.argv[3])
fracT = float(sys.argv[4])

seqLen = int(sys.argv[5])

mySeq = ''
for i in range(0,seqLen):
  rndnum = random.random()

  nt = ''
  if rndnum < fracA :
    nt = 'A'
  if rndnum >= fracA and rndnum < fracA+fracC:
    nt = 'C'
  if rndnum >= fracA+fracC and rndnum < fracA+fracC+fracG:
    nt = 'G'
  if rndnum >= fracA+fracC+fracG:
    nt = 'T'
  
  mySeq += nt

print("Seq = " + mySeq)

cnt_dic = {}
for nt in 'ACGT':
  cnt_dic[nt] = 0

for i in range(0,len(mySeq)):
  nt = mySeq[i]
  cnt_dic[nt] += 1

for nt in 'ACGT':
  outStr = '%s\t%d\t%.2f' %(nt, cnt_dic[nt], cnt_dic[nt]/len(mySeq))
  print(outStr)
