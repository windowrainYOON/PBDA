#!/usr/bin/env python3

import random
import math

seqLen = 100
seqFractionDic = {}
seqStr = 'ACGT'
seqList = ["A", "C", "G", "T"]
argv = [0.4, 0.1, 0.1, 0.4]

for i in seqStr:
    seqFractionDic[i] = math.floor(float(argv[seqStr.find(i)])*seqLen)

seq = []
for i in range(0, seqLen):
    choiceList = seqList
    for j in choiceList:
        if seqFractionDic[j] == 0:
            choiceList.remove(j)
    ranSeq = random.choice(choiceList)
    seq.extend([ranSeq])
    seqFractionDic[ranSeq] = seqFractionDic[ranSeq] - 1


print("Seq = ", end='')
for i in range(0, len(seq)):
    print(seq[i], end='')
print('')
for i in seqStr:
    print('%s\t%-d\t%.2f' % (i, seq.count(i), seq.count(i)/seqLen))