#!/usr/bin/env python3

import sys

kmer = int(sys.argv[1])
fpath = sys.argv[2]

# 여러개의 seq가 포함된 fa file을 읽는 함수
def multiple_seq_reader(fpath):
  seqdic = {}
  name, seq = '', ''
  for line in open(fpath):
    if line[0] == '>':
      if len(seq) > 0:
        seqdic[name] = seq
        seq = ''
      name = line[1:].rstrip()
    else:
      seq += line.upper().rstrip()
  seqdic[name] = seq
  return seqdic

# 같은 index에서 겹치는 kmer의 수를 count하는 함수
def seq_overlap_counter(seq1, seq2, kmer):
  count_result = 0
  for i in range(0, len(seq1) - kmer):
    if seq1[i:i+kmer] == seq2[i:i+kmer]:
      # if seq1[i:i+kmer] not in count_result: count_result[seq1[i:i+kmer]] = 0
      # count_result[seq1[i:i+kmer]] += 1
      count_result += 1
  return count_result

seqdic = multiple_seq_reader(fpath=fpath)

seqs = list(seqdic.values())

overlap = {}
for i in range(1, kmer+1):
  result = seq_overlap_counter(seq1=seqs[0], seq2=seqs[1], kmer=i)
  overlap[i] = result

for k, lap in overlap.items():
  print("%*d %s (%s)" %(len(str(kmer)), k, chr(0x258c)*lap, lap))