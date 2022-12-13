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

#string sequence를 kmer 단위로 잘라주는 함수
def kmer_slicer(seq, kmer):
  result = [seq[i:i+kmer] for i in range(0, len(seq), kmer)]
  return result

#string 두개를 받아서 같은 index에 같은 알파벳이 몇개나 있는지 count해서 반환하는 함수
def similarity_checker(str1, str2):
  similarity_count = 0
  for i in range(len(str1)):
    if str1[i] != str2[i]: continue
    if str1[i] == str2[i]: similarity_count += 1
  return similarity_count



seqdic = multiple_seq_reader(fpath)
sliced_seq = {}
for name, seq in seqdic.items():
  sliced_seq[name] = kmer_slicer(seq=seq, kmer=kmer)

seqs = list(sliced_seq.values())
seq1 = seqs[0]
seq2 = seqs[1]

similarity_count = 0
similar_kmers = []
for kmer1, kmer2 in zip(seq1, seq2):
  count = similarity_checker(kmer1, kmer2)
  if count > similarity_count: 
    similarity_count = count
    similar_kmers = []
    similar_kmers.append([kmer1, kmer2])
  if count == similarity_count:
    similar_kmers.append([kmer1, kmer2])

print("유사도 높은 염기서열 :", similar_kmers)
print("유사도: %d" %(similarity_count))

