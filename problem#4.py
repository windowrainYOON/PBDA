#!/usr/bin/env python3

import sys

fpath = sys.argv[1]
slen = int(sys.argv[2])

#string으로부터 모든 sub의 index를 리스트로 반환하는 함수
def find_all(_str, sub):
  result = [i for i in range(len(_str)) if _str.startswith(sub, i)]
  if result == [] : result.append(-1)
  return result

#sequence를 받아 N, intron을 제거하고 exon만 추출해서 반환하는 함수
def exon_filter(seq_string):
  seq_string = seq_string.rstrip().replace('N', '')
  result_seq = ''
  for i in seq_string:
    if i.islower(): continue
    if i.isupper(): result_seq += i
  return result_seq

def gene_indexer (exon, start_index, gene_index):
  result = {}
  scodon_index = find_all(_str=exon, sub='AUG')
  gene_index_func = gene_index
  if scodon_index == [-1]: 
    return result
  if scodon_index != [-1]:
    for scodon_index in scodon_index:
      triplet_string = exon[scodon_index:]
      triplet_data = [triplet_string[i:i+3] for i in range(0, len(triplet_string), 3)]
      index = [i for i, ele in enumerate(triplet_data) if ele == 'TAA' or ele == 'TAG' or ele == 'TGA']
      index.sort()
      if index != []:
        result.update({gene_index_func : {"gene index":start_index+scodon_index, "gene size":3*index[0]}})
        gene_index_func += 1
      if index == []:
        result.update({"gene index":start_index+scodon_index, "gene size":-1})
        gene_index_func += 1
  return result

# seq를 한줄씩 읽어 100bp 미만만큼 저장하고, 저장된 seq에 대해 매개변수로 받은 함수를 적용해 결과를 반환하는 함수
def seq_reader(seq_path, save_len):
  exon = ''
  index = 0
  gene_num = 1
  result = {}
  for line in open(seq_path):
    if line[0] == '>':
      continue
    if line[0] != '>':
      if len(exon) < save_len:
        exon += exon_filter(line)
      if len(exon) >= save_len:
        gene_found = gene_indexer(exon=exon, start_index=index, gene_index=gene_num)
        if gene_found != {}:
          result.update(gene_found)
          gene_num += len(list(gene_found.keys()))
        index += len(exon)
        exon = ''
  return result

result = seq_reader(seq_path=fpath, save_len=slen)
print(result)
