#!/usr/bin/env python3

import sys

fpath_pattern = sys.argv[1]
fpath_multiple_seq = sys.argv[2]
match_score = sys.argv[3]
mismatch_scoree = sys.argv[4]

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

def pattern_reader(ppath):
  mypattern = []
  for line in open(ppath):
      mylist = line.split()
      mydic = {}
      for (i, nt) in enumerate('ACGT'):
          mydic[nt] = float(mylist[i])
      mypattern.append(mydic)
  return mypattern

def pscore_calulator(seq, mypattern):
  max_score = 0
  for i in range(0, len(seq) - len(mypattern) + 1):
      score = 1
      for j in range(0, len(mypattern)):
          score *= mypattern[j][seq[i+j]]
      if score >= max_score:
          max_score = score
  return max_score

def combination(list):
  result = []
  for i in range(len(list)-1):
    for j in range(i+1, len(list)):
      result.append([list[i], list[j]])
  return result

def mscore_calulator(seq1, seq2, match, mismatch):
  score = 0
  for i in range(0, len(seq1)):
    if seq1[i] == seq2[i]:
      score += int(match)
    if seq1[i] != seq2[i]:
      score -= int(mismatch)
  return score

mypattern = pattern_reader(ppath=fpath_pattern)
seq_dic = multiple_seq_reader(fpath=fpath_multiple_seq)
seq_list = list(seq_dic.values())

combinations = combination(seq_list)

score = 0
for list in combinations:
  score += mscore_calulator(list[0], list[1], match_score, mismatch_scoree)

print(score/len(list(seq_dic.keys())))