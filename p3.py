#!/usr/bin/env python3

from longseq3 import seq

seqDic = {}
seqList = list(seq)
seqNum = len(seqList)
for i in 'ACGT':
    for j in 'ACGT':
        seqDic[i+j]=0

for i in range(len(seqList)-1):
    seqDic[seqList[i]+(seqList[i+1])] += 1

_width = 0
for i in seqDic:
    _seqWidth = len(str(seqDic[i]))
    if _seqWidth >=_width:
        _width = _seqWidth

print(seqDic)

seqKeyList = []
for i in seqDic:
    seqKeyList.append(seqDic[i])
seqKeyList.sort()

print("Min = %d" %(seqKeyList[0]))
print("Max = %d" %(seqKeyList[-1]))
print("Avg = %.2f" %(sum(seqKeyList)/len(seqKeyList)))