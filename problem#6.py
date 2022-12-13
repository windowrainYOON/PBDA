#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

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

# 두 seq를 읽어 같은 index에 존재하는 kmer가 몇개가 있는지 count하고 가장 신 kmer를 반환하는 함수
def seq_overlap_counter(seq1, seq2, kmer):
  count_result = 0
  maxkmer = ''
  for i in range(0, len(seq1) - kmer):
    if seq1[i:i+kmer] == seq2[i:i+kmer]:
      count_result += 1
      if len(maxkmer) < kmer: maxkmer = seq1[i:i+kmer]
  return count_result, maxkmer

seqdic = multiple_seq_reader(fpath=fpath)
seqs = list(seqdic.values())

# 모든 경우의 수에 대해서 overlap을 검사
overlap = {}
result_maxkmer = ""
for i in range(1, len(seqs[0])+1):
  result, maxkmer = seq_overlap_counter(seq1=seqs[0], seq2=seqs[1], kmer=i)
  if len(result_maxkmer) < len(maxkmer): result_maxkmer = maxkmer
  overlap[i] = result

print("k\t개수")
for kmer, count in overlap.items():
  if count != 0:
    print("%d\t%d" %(kmer, count))
print("가장 긴 k-mer : %s" %(result_maxkmer))


