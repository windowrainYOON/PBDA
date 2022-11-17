#!/usr/bin/env python3

from longseq3 import seq

_maxBet = 10

seqTDic = {}
for i in range(1, _maxBet+1):
    seqTDic[i] = 0

for i in range(1, _maxBet+1):
    for j in range(1, len(seq)-i):
        countT = 0
        if seq[j] == "T":
            for a in range(1, i+1):
                if seq[j+a] == "T":
                    countT += 1
                else :
                    continue
        if countT == i:
            seqTDic[i] += 1
totalNum = 0
for i in seqTDic:
    if seqTDic[i] != 0:
        print('%s\t%d' % (i, seqTDic[i]))
    totalNum += seqTDic[i]

print('Total Number: %d' %(totalNum))
print('Total Length: %d' %(len(seq)))