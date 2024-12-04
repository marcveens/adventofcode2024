import os
from is_list_safe import is_list_safe
from is_list_almost_safe import is_list_almost_safe

script_dir = os.path.dirname(os.path.abspath(__file__))

file = open(os.path.join(script_dir, 'input.txt'), 'r')
content = file.read()

safe_records = 0
almost_safe_records = 0

split_string = content.split("\n")

for record in split_string:
  split_record = record.split(" ")
  int_list = [int(item) for item in split_record]
  
  is_safe = is_list_safe(int_list)
  
  if is_safe == True:
    safe_records += 1
    
print(f"Part 1: {safe_records}")

# Part 2
for record in split_string:
  split_record = record.split(" ")
  int_list = [int(item) for item in split_record]
  
  if is_list_almost_safe(int_list):
    almost_safe_records += 1
    
print(f"Part 2: {almost_safe_records}")