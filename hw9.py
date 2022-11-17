#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

seqdic = {}
name = ''
seq = {x:0 for x in 'ACGT'}

#line 별로 염기를 뽑아 nt별 갯수 count
for line in open(fpath):
  
  # fa 제목 처리
  if line[0] == '>': 
    #저장된 염기를 name key에 할당
    if seq != {x:0 for x in 'ACGT'}:
      seqdic[name] = seq 
      seq = {x:0 for x in 'ACGT'} # seq 초기화

    name = line[1:].rstrip() # seq 이름 (name) 저장

  # fa 염기 처리
  if line[0] != '>':
    seqline = line.rstrip()
    for i in 'ACGT':
      seq[i] += line.rstrip().count(i)

seqdic[name] = seq # 마지막 seqdic item 저장

#염기 갯수를 염기분율로 치환
for name in seqdic.keys():
  sum = 0
  for i in seqdic[name].keys():
    sum += seqdic[name][i]
  for i in seqdic[name].keys():
    seqdic[name][i] = seqdic[name][i]/sum

#name 간의 조합 및 조합별 result 추출
result = {}
seqdicKeys = list(seqdic.keys())
for i in range(len(seqdicKeys)):
  for j in seqdicKeys[i+1:]:
    name1 = seqdicKeys[i]
    name2 = j
    sum = 0
    for nt in 'ACGT':
      sum += seqdic[name1][nt]*seqdic[name2][nt]
    num = round(sum/4, 6) #염기 분율 곱을 소수점 6자리 출력으로 제한
    pair = name1+':'+name2

    #같은 분율을 가진 pair끼리 정리
    if num in result.keys():
      result[num].append(pair)
    if not num in result.keys():
      result[num] = [pair]

#출력
for i in result.keys():
  print(i, end=' ')
  for j in result[i]:
    print(j, end=' ')
  print("")