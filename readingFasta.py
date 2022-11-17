#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

seqdic = {}
name = ''
seq = ''

for line in open(fpath):
  if line[0] == '>': 
    if len(seq) > 0:
      seqdic[name] = seq #첫번째 줄 처리
      seq = '' # seq 초기화

    name = line[1:].rstrip() # seq 이름 (name) 저장

  else:
    seq += line.rstrip() # seq data 저장

seqdic[name] = seq # 마지막 seqdic item 저장

for name in seqdic.keys():
    seq = seqdic[name]
    print(name + " : " + seq)