#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

genedic = {}
seq = ''
for line in open(fpath):
  if line.rstrip().isalpha():
    seq += line.rstrip()
  if not line.rstrip().isalpha():
    [_name, _start, _end] = line.split()
    genedic[_name] = [int(_start), int(_end)]

_format = len(str(len(seq)))


geneCount = [0 for x in seq]

for indexlist in genedic.values():
  for index in range(indexlist[0], indexlist[1]+1):
    geneCount[index-1] += 1


result = {}
startIndex, endIndex = 1, -1
for i in range(len(geneCount)-1):
  if geneCount[i] == geneCount[i+1]:
    if i == (len(geneCount)-2):
      endIndex = i+2
    continue
  if geneCount[i] != geneCount[i+1]:
    endIndex = i+1
    key = "%*d - %*d" % (_format, startIndex, _format, endIndex) 
    result[key] = geneCount[i]
    startIndex = i+2
    if i == (len(geneCount)-2):
      startIndex = i+2
      endIndex = i+2
      key = "%*d - %*d" % (_format, startIndex, _format, endIndex) 
      result[key] = geneCount[i+1]

for (key, value) in result.items():
  print("%s : %d %s" %(key, value, chr(0x258C)*value))