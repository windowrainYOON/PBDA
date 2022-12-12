#!/usr/bin/env python3

import sys

kmer = int(sys.argv[1])
fpath = sys.argv[2]

# 단일 seq fa file을 읽는 함수
def single_seq_reader(fpath):
  seq = ''
  for line in open(fpath):
    if line[0] == '>':
      continue
    else:
      seq += line.upper().rstrip()
  return seq

# seq로부터 kmer를 반환하는 함수
def get_kmers_by_seq(seq, kmer):
  kmers = []
  for i in range(len(seq) - kmer):
    get_kmer = ''
    for j in range(kmer):
      get_kmer += seq[i+j]
    kmers.append(get_kmer)
  return list(set(kmers))

#list에서 원소들 간의 gap을 계산해주는 함수
def gaps_calculator(list):
  list.sort(reverse=True)
  gaps = []
  for i in range(len(list)-1):
      gaps.append(list[i]-list[i+1])
  return gaps

# seq에서 kmer에 해당하는 index를 추출해 index 간 gap을 계산해주는 함수
def kmer_gap_calulator(seq, kmers):
  gaps_dic = {}
  for i in kmers:
    indexs = [n for n in range(len(seq)) if seq.find(i, n) == n]
    gaps_dic[i] = gaps_calculator(indexs)
  return gaps_dic


orf = single_seq_reader(fpath=fpath)
kmers = get_kmers_by_seq(seq=orf, kmer=kmer)
gap_dic = kmer_gap_calulator(seq=orf, kmers=kmers)

for kmer, gaps in gap_dic.items():
  if len(gaps) == 0: continue
  gap_avg = sum(gaps)/len(gaps)
  print("%s : %s" %(kmer, gap_avg))