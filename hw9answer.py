#!/usr/bin/env python3

import sys

fpath = sys.argv[1]

seqdic = {}
name, seq = '', ''
for line in open(fpath):
  if line[0] == '>':
    if len(seq) > 0:
      seqdic[name] = seq
      seq = ''
    name = line[1:].rstrip()
  else:
    seq += line.rstrip()

seqdic[name] = seq


fracdic = {}
for name in seqdic.keys():
  seq = seqdic[name]

  ntdic = {}
  for nt in 'ACGT':
    ntdic[nt] = 0
  
  for nt in seq:
    ntdic[nt] += 1

  frac = []
  for nt in 'ACGT':
    frac.append(ntdic[nt]/len(seq))
  
  fracdic[name] = frac


names = sorted(list(seqdic.keys()))

final_dic = {}
for i in range(0, len(names)-1):
  name1 = names[i]
  frac1 = fracdic[name1]
  for j in range(i+1, len(names)):
    name2 = names[j]
    frac2 = fracdic[name2]

    score = 0
    for k in range(0, 4):
      score += frac1[k] * frac2[k]
    score /= 4

    val = name1 + ':' + name2
    if score in final_dic:
      final_dic[score].append(val)
    else:
      final_dic[score] = [val]


for score in sorted(final_dic.keys()):
  print('%.6f' % score, end=' ')
  for pair in final_dic[score]:
    print(pair, end=' ')
  print()