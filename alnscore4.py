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


def combination(list):
  result = []
  for i in range(len(list)-1):
    for j in range(i+1, len(list)):
      result.append([list[i], list[j]])
  return result

def scoreCalulator(seq1, seq2):
  match = 0
  mismatch = 0
  indels = 0
  nongapseq = 0
  for i in range(0, len(seq1)):
    if seq1[i] != '-' and seq2[i] != '-' : 
      nongapseq += 1
    if seq1[i] == '-' or seq2[i] == '-':
      indels += 1
    elif seq1[i] == seq2[i]:
      match += 1
    elif seq1[i] != seq2[i]:
      mismatch += 1
  return (match * 2) + (-1 * indels)


seqdic = fastaHandler(fpath)
combkeys = combination(list(seqdic.keys()))
sum = 0
for keylist in combkeys:
  sum += scoreCalulator(seqdic[keylist[0]], seqdic[keylist[1]])

print(sum/len(combkeys))


