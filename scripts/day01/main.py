import os
from typing import List

script_dir = os.path.dirname(os.path.abspath(__file__))

file = open(os.path.join(script_dir, 'input.txt'), 'r')
content = file.read()

list_01: List[int] = []
list_02: List[int] = []
distances: List[int] = []

split_string = content.split("\n")

for record in split_string:
  split_record = record.split("   ")
  
  list_01.append(int(split_record[0]))
  list_02.append(int(split_record[1]))
  
list_01.sort()
list_02.sort()

for idx, record in enumerate(list_01):
  record_02 = list_02[idx]
  
  if record < record_02:
    distances.append(record_02 - record)
  elif record > record_02:
    distances.append(record - record_02)
  else:
    distances.append(0)
    
total = sum(distances)

print(f"Part 1: {total}")

# Part 2
similarity_score_list: List[int] = []

for record in list_01:
  occurrences = list_02.count(record)
  
  if (occurrences > 0):
    similarity_score_list.append(record * occurrences)
    
similarity_total = sum(similarity_score_list)

print(f"Part 2: {similarity_total}")