#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

#fasta file로부터 염기와 유전자 이름을 추출해서 dictionary에 저장 
def fastaHandler(fpath):
  seqdic = {}
  name, seq = '', ''
  for line in open(fpath):
    if line[0] == '>':
      if len(seq) > 0:
        seqdic[name] = list(seq)
        seq = ''
      name = line[1:].rstrip()
    else:
      seq = line.rstrip()

  seqdic[name] = list(seq)

  return seqdic

seqdic = fastaHandler(fpath)
print(seqdic)


