#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

#sequence를 받아 N, intron을 제거하고 exon만 추출해서 반환하는 함수
def exon_filter(seq_string):
  seq = seq.rstrip().replace('N', '')
  result_seq = ''
  for i in seq_string:
    if i.islower(): continue
    if i.isupper(): result_seq += i
  return result_seq

# seq를 한줄씩 읽어 100bp 미만만큼 저장하고, 저장된 seq에 대해 매개변수로 받은 함수를 적용해 결과를 반환하는 함수
def seq_reader(seq_path, func):
  exon = ''
  index = 0
  result = {}
  for line in open(seq_path):
    if line[0] == '>':
      continue
    if line[0] != '>':
      if len(exon) < 100:
        exon += exon_filter(line)
        index += len(line)
      if len(exon) >= 100:
        result.update(func(exon))
        exon = exon_filter(line)
        index += len(line)
      # if exon == '':
      #   line1 = line.upper().rstrip().replace('N', '')
      #   index += len(line)
      #   continue
      # if line1 != '':
      #   if line2 == '': 
      #     line2 = line.upper().rstrip().replace('N', '')
      #     scores.update(func(line1=line1, line2=line2))
      #     index += len(line)
      #   if line2 != '':
      #     line1 = line2
      #     line2 = line.upper().rstrip().replace('N', '')
      #     scores.update(func(line1=line1, line2=line2))
      #     index += len(line)
  return result

def gene_indexer (exon, start_index):
  result = {}
  if exon.find() == -1: return result
  if exon.find() != -1:
    
