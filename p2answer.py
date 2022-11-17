#!/usr/bin/env python3

import sys

fpath = sys.argv[1]
maxLen = int(sys.argv[2])
mySeq = open(fpath).read().rstrip()

dic_len = {}
for i in range(1, maxLen+1):
  dic_len[i] = 0

start = -1

for i in range(0, len(mySeq)):
  nt = mySeq[i]

  if nt == 'T':
    if start == -1:
      start = i
    else:
      cnt = i - start -1
      if cnt > 0 and cnt <= maxLen:
        dic_len[cnt] += 1
      start = i

maxCnt = 0
for i in range(1, maxLen+1):
  cnt = dic_len[i]
  if cnt > maxCnt:
    maxCnt = cnt

totalNum, totalLen = 0, 0

for i in range(1, maxLen+1):
  cnt = dic_len[i]
  totalNum += cnt
  totalLen += i * cnt
  if cnt > 0:
    print('%d\t%*d' %(i, len(str(maxCnt)), cnt))
print("Total Number: "+ str(totalNum))
print("Total Length: "+ str(totalLen))