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
        seqdic[name] = seq
        seq = ''
      name = line[1:].rstrip()
    else:
      seq = line.rstrip()

  seqdic[name] = seq

  return seqdic

seqdic = fastaHandler(fpath)
keys = list(seqdic.keys())
seq1 = seqdic[keys[0]]
seq2 = seqdic[keys[1]]

match = 0
nongapseq = 0
for i in range(0, len(seq1)):
  if seq1[i] != '-' and seq2[i] != '-' : 
    nongapseq += 1
  if seq1[i] == '-' or seq2[i] == '-':
    continue
  if seq1[i] == seq2[i]:
    match += 1

print(match/nongapseq)

