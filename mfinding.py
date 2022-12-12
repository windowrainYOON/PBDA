#!/usr/bin/env python3

import sys

pattern_path = sys.argv[1]
seq_path = sys.argv[2]
cutoff = float(sys.argv[3]) 

# pattern path를 받아서 binding pattern의 길이를 계산해주는 함수
def patternlen (pattern_path):
  motiflen = 0
  for line in open(pattern_path):
    motiflen += 1
  return motiflen

# pattern path와 그 길이에 해당하는 motif를 받아서 score를 계산해주는 함수
def seq_score (motif, pattern_path):
  line_index = 0
  score = 1
  for line in open(pattern_path):
    line_list = line.split(" ")
    if motif[line_index] == 'A':
      score *= float(line_list[0])
    if motif[line_index] == 'C':
      score *= float(line_list[1])
    if motif[line_index] == 'G':
      score *= float(line_list[2])
    if motif[line_index] == 'T':
      score *= float(line_list[3])
    line_index += 1
  return score

# seq line 두개, 패턴, cutoff, 첫번째 line의 index를 받아 두 line에 대한 score를 계산하고 cutoff이상의 score와 해당 index를 dictionary로 반환하는 함수
def score_calculator (line1, line2, pattern_path, cutoff, line1_index):
  seq_line = line1+line2
  motiflen = patternlen(pattern_path)
  score_index = {}
  for i in range(0, len(seq_line)-motiflen+1):
    motif = seq_line[i:i+motiflen]
    score = seq_score(motif, pattern_path)
    if score >= cutoff:
      score_index[line1_index+i+1] = [score, motif]
  return score_index
    
def seq_reader(seq_path):
  line1 = ''
  line2 = ''
  index = 0
  scores = {}
  for line in open(seq_path):
    if line[0] == '>':
      continue
    if line[0] != '>':
      if line1 == '':
        line1 = line.upper().rstrip().replace('N', '')
        index += len(line)
        continue
      if line1 != '':
        if line2 == '': 
          line2 = line.upper().rstrip().replace('N', '')
          scores.update(score_calculator(line1=line1, line2=line2, pattern_path=pattern_path, cutoff=cutoff, line1_index=index))
          index += len(line)
        if line2 != '':
          line1 = line2
          line2 = line.upper().rstrip().replace('N', '')
          scores.update(score_calculator(line1=line1, line2=line2, pattern_path=pattern_path, cutoff=cutoff, line1_index=index))
          index += len(line)
  return scores

score_dic = seq_reader(seq_path=seq_path)
for index, list in score_dic.items():
  target_seq_len = patternlen(pattern_path)
  print("Index : %s Sequence : %s Score : %s" %(index, list[1], list[0]))

      

    
