import os

def get_xmas(fileName):
  file_contents = get_file_contents(fileName)
  to_find = "XMAS"
  
  total = 0
  
  total += find_horizontal(file_contents, to_find)
  total += find_vertical(file_contents, to_find)
  total += find_diagonal(file_contents, to_find)
  
  return total

def find_horizontal(body, to_find):
  total = 0
  
  reversed_to_find = to_find[::-1]
  
  total += body.count(to_find)
  total += body.count(reversed_to_find)
  
  return total

def find_vertical(body, to_find):
  total = 0
  
  matrix = get_matrix(body)
  
  def condition(prev_match_row, prev_match_col, row, col):
    return prev_match_col == col and row == prev_match_row + 1
  
  total += recursive_find(matrix, to_find, condition)
  total += recursive_find(matrix, to_find[::-1], condition)
    
  return total

def find_diagonal(body, to_find):
  total = 0
  
  matrix = get_matrix(body)
  
  def forward_condition(prev_match_row, prev_match_col, row, col):
    return prev_match_col + 1 == col and row == prev_match_row + 1
  
  def reverse_condition(prev_match_row, prev_match_col, row, col):
    return prev_match_col - 1 == col and row == prev_match_row - 1
  
  # Search for XMAS
  total += recursive_find(matrix, to_find, forward_condition)
  total += recursive_find(list(reversed(matrix)), to_find, reverse_condition)
  
  # # Search for SAMX 
  total += recursive_find(matrix, to_find[::-1], forward_condition)
  total += recursive_find(list(reversed(matrix)), to_find[::-1], reverse_condition)
  
  return total

def recursive_find(matrix, to_find, condition, start_row=0, start_col=0):
  found_words = 0
  
  for matrix_item in matrix:
    word = ""
    
    if matrix_item.get("char") == to_find[0]:  
      word += matrix_item.get("char")
      
      next_item = [item for item in matrix if 
        condition(matrix_item.get("row"), matrix_item.get("col"), item.get("row"), item.get("col"))]
      
      print(f"next item {next_item} {to_find[1]}")
      
      if next_item and next_item[0].get("char") == to_find[1]:
        word += next_item[0].get("char")
        start_row = next_item[0].get("row")
        start_col = next_item[0].get("col")
        
        next_item = [item for item in matrix if 
          condition(start_row, start_col, item.get("row"), item.get("col"))]
        
        if next_item and next_item[0].get("char") == to_find[2]:
          word += next_item[0].get("char")
          start_row = next_item[0].get("row")
          start_col = next_item[0].get("col")
          
          next_item = [item for item in matrix if 
            condition(start_row, start_col, item.get("row"), item.get("col"))]
        
          if next_item and next_item[0].get("char") == to_find[3]:
            word += next_item[0].get("char")
            print(f"word: {word}")
            found_words += 1
  
   
  return found_words     


def get_matrix(body):
  split_body = body.split("\n")
  
  matrix = []
  
  for row_idx, row in enumerate(split_body):
    characters = list(row)
    
    for col_idx, char in enumerate(characters):
      matrix.append({
        "row": row_idx,
        "col": col_idx,
        "char": char
      })
      
  return matrix

def get_file_contents(fileName):
  script_dir = os.path.dirname(os.path.abspath(__file__))

  file = open(os.path.join(script_dir, fileName), 'r')
  content = file.read()
  
  return content
