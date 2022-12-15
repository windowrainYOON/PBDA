#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

# 단일 seq fa file을 읽는 함수
def single_seq_reader(fpath):
  seq = ''
  for line in open(fpath):
    if line[-1].rstrip().isnumeric():
      continue
    else:
      seq += line.upper().rstrip()
  return seq

def gene_reader(fapth):
  gene = {}
  for line in open(fapth):
    data = line.rstrip()
    if data[-1].isalpha(): continue
    if data[-1].isnumeric():
      _list = data.split()
      gene[_list[0]] = [int(_list[1]), int(_list[2])]
  return gene


def gene_integrator(seqlen, gene_dic):
  result = {}
  start, final = int(seqlen), 0
  name = 1
  for index_list in gene_dic.values():
    start = index_list[0]
    if final <= index_list[-1]:
      final = index_list[-1]
    for index_list2 in gene_dic.values():
      if index_list2[0] < start: start = index_list2[0]
    for index_list2 in gene_dic.values():
      if index_list2[0] > final: 
        result[name] = [start, final]
        start = index_list2[0]
        final = index_list2[-1]
        name += 1
        for index_list2 in gene_dic.values():
          if index_list2[-1] > final: 
            final = index_list2[-1]
            result[name] = [start, final]
        break
  return result

seq = single_seq_reader(fpath=fpath)
genes_initial = gene_reader(fapth=fpath)
genes_integrated = gene_integrator(seqlen=len(seq), gene_dic=genes_initial)

result = list(genes_integrated.values())
result.sort()
format = len(str(len(seq)))
for list in result:
  start = int(list[0])
  final = int(list[1])
  print("%*d - %*d : %s" %(format, start, format, final, seq[start:final+1]))


