#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

#fpath를 받아 {gene 이름 : [시작인덱스, 끝 인덱스], ...}, [0,0,0,...] (seq 길이만큼 0을 리스트에 담음) 으로 반환하는 함수
def getSeqAndGeneData(fpath):
  genedic = {}
  seq = ''
  for line in open(fpath):
    if line.rstrip().isalpha(): #seq인 경우 seq data string으로 저장
      seq += line.rstrip()
    if not line.rstrip().isalpha(): #gene인 경우 genedic에 {gene 이름 : [시작인덱스, 끝 인덱스], ...} 저장
      [_name, _start, _end] = line.split()
      genedic[_name] = [int(_start), int(_end)]
  numAlignFormat = len(str(len(seq)))
  geneCount = [0 for x in seq]
  return genedic, geneCount, numAlignFormat

#nt별로 gene이 몇개가 겹치는지 색인해서 geneCount 리스트의 해당 index에 저장
def countGeneLocation(genedic, geneCount):
  for indexlist in genedic.values():
    for index in range(indexlist[0], indexlist[1]+1):
      geneCount[index-1] += 1
  return geneCount

#연속된 geneCount 값을 가진 원소들을 result 리스트의 한 key의 value로 align
def alignResult(geneCount, alignNum):
  result = {}
  startIndex, endIndex = 1, -1
  for i in range(len(geneCount)-1):
    if geneCount[i] == geneCount[i+1]:
      if i == (len(geneCount)-2):
        endIndex = i+2
      continue
    if geneCount[i] != geneCount[i+1]:
      endIndex = i+1
      key = "%*d - %*d" % (alignNum, startIndex, alignNum, endIndex) 
      result[key] = geneCount[i]
      startIndex = i+2
      if i == (len(geneCount)-2):
        startIndex = i+2
        endIndex = i+2
        key = "%*d - %*d" % (alignNum, startIndex, alignNum, endIndex) 
        result[key] = geneCount[i+1]
  return result


#파일 경로로부터 한줄씩 seq와 gene infomation을 추출
genedic, geneCount, numAlignFormat = getSeqAndGeneData(fpath)

#gene의 위치 index를 기반으로 nt별로 몇 레이어의 gene이 겹쳐있는지 추출
geneCount = countGeneLocation(genedic, geneCount)

#연속된 geneCount 값을 가진 원소들을 result 리스트의 한 key의 value로 align
result = alignResult(geneCount = geneCount, alignNum = numAlignFormat)

#print data
bar = chr(0x258C)
for (key, value) in result.items():
  valueFormat = len(str(sorted(list(result.values()))[-1]))
  print("%s : %*d %s" %(key, valueFormat, value, bar*value))