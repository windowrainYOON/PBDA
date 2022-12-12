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

#seq string을 뒤집어 반환하는 함수
def seq_reverser(seq):
  return seq[::-1]

def get_kmers_by_seq(seq, kmer):
  kmers = []
  for i in range(len(seq) - kmer):
    get_kmer = ''
    for j in range(kmer):
      get_kmer += seq[i+j]
    kmers.append(get_kmer)
  return list(set(kmers))

orf1 = single_seq_reader(fpath=fpath)
orf2 = seq_reverser(orf1)

kmers1 = get_kmers_by_seq(seq=orf1, kmer=kmer)
kmers2 = get_kmers_by_seq(seq=orf2, kmer=kmer)

_intersection = list(set(kmers1) & set(kmers2))

print(_intersection)