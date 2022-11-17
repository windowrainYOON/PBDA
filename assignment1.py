#!/usr/bin/env python3

import sys
import math

IndexSeq = list(str(sys.argv[1]))
graphXlen = int(sys.argv[2])
AASeq = open(sys.argv[3]).read().rstrip()

sepUnit = math.floor(len(AASeq)/graphXlen)

portionDic = {}
for i in range(1, graphXlen+1):
  portionDic[i] = 0

for i in range(graphXlen+1):
  if i == graphXlen:
    seq = list(AASeq[i*graphXlen:])
  seq = list(AASeq[i*sepUnit : i*sepUnit+sepUnit])
  portion = 0
  for j in IndexSeq:
    if j in seq:
      portion += seq.count(j)
  portionDic[i+1] = portion

for i in portionDic:
  portionDic[i] = round((portionDic[i]/sepUnit)*100, 3)

print("AA Sequence length : %d" %(len(AASeq)))

for i in portionDic:
  bars = chr(0x258C)*math.floor(portionDic[i])
  print("~ %*d : %s (%.3f%%)" %(len(str(graphXlen*sepUnit)), (i-1)*sepUnit+sepUnit, bars, portionDic[i]))

