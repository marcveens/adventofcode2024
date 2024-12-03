import re

def get_mul_instructions(str):
  mul_pattern = r"mul\(\d+,\d+\)"
  action_pattern = r"do\(\)|don't\(\)"
  
  mul_indices = [(match.start(), match.end()) for match in re.finditer(mul_pattern, str)]
  mul_matches = [str[start:end] for start, end in mul_indices]
  
  action_indices = [(match.start(), match.end()) for match in re.finditer(action_pattern, str)]
  action_matches = [str[start:end] for start, end in action_indices]

  list = []
  enabled_list = []
  
  for idx, match in enumerate(mul_matches):
    stripped_match = match.replace("mul(", "").replace(")", "")
    split_match = stripped_match.split(",")
    numbers = [int(item) for item in split_match]
    
    outcome = 1
    
    for number in numbers:
      outcome = outcome * number
    
    list.append({
      "start_index": mul_indices[idx][0],
      "end_index": mul_indices[idx][1],
      "raw": match,
      "values": numbers,
      "outcome": outcome
    })
    
  
  for idx, match in enumerate(action_matches):
    list.append({
      "start_index": action_indices[idx][0],
      "end_index": action_indices[idx][1],
      "raw": match,
      "values": 0,
      "outcome": 0
    })
    
  # Sort by start_index
  sorted_list = sorted(list, key=lambda x: x["start_index"])
  
  # Loop over list and disable values that come after "don't()"
  disable_processing = False
  prev_item = None
  for idx, item in enumerate(sorted_list):
    if prev_item == None:
      prev_item = item
      
      # In case of idx 0, also add to list 
      enabled_list.append(item)
      
      continue
    
    if prev_item.get("raw") == "don't()":
      disable_processing = True
    
    if prev_item.get("raw") == "do()":
      disable_processing = False
      
    if not disable_processing:
      enabled_list.append(item)
    
    prev_item = item
    

  mapped_list = [
    {
      "raw": item.get("raw"),
      "values": item.get("values"),
      "outcome": item.get("outcome")
    }
    for item in enabled_list
  ]
  
  return mapped_list