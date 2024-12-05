import os

def get_xmas(file_name):
  file_contents = get_file_contents(file_name)
  to_find = "MAS"
  
  total = 0
  
  total += find_diagonal(file_contents, to_find)
  
  return total

def find_diagonal(body, to_find):
  total = 0
  
  matrix = get_matrix(body)
  
  def top_bottom_right_condition(prev_match_row, prev_match_col, row, col):
    return prev_match_col + 1 == col and row == prev_match_row + 1
  
  def top_bottom_left_condition(prev_match_row, prev_match_col, row, col):
    return prev_match_col - 1 == col and row == prev_match_row + 1
  
  # Search for XMAS
  # Top to bottom, right
  # total += recursive_find(matrix, to_find, top_bottom_right_condition)
  # # Top to bottom, left
  # total += recursive_find(matrix, to_find, top_bottom_left_condition)
  
  # # Search for SAMX 
  # # Bottom to top, left
  # total += recursive_find(matrix, to_find[::-1], top_bottom_right_condition)
  # # Bottom to top, right
  # total += recursive_find(matrix, to_find[::-1], top_bottom_left_condition)
  
  total += recursive_find(matrix)
  
  return total

def recursive_find(matrix):
  found_words = 0
  
  for matrix_item in matrix:
    if matrix_item.get("char") == "A":
      row_index = matrix_item.get("row")
      col_index = matrix_item.get("col")
      
      left_top = [item for item in matrix if item.get("row") == row_index - 1 and item.get("col") == col_index - 1]
      right_top = [item for item in matrix if item.get("row") == row_index - 1 and item.get("col") == col_index + 1]
      left_bottom = [item for item in matrix if item.get("row") == row_index + 1 and item.get("col") == col_index - 1]
      right_bottom = [item for item in matrix if item.get("row") == row_index + 1 and item.get("col") == col_index + 1]
      
      # find M** in previous line
      if left_top and right_top and left_bottom and right_bottom:
        if left_top[0].get("char") == "M" and right_bottom[0].get("char") == "S" and left_bottom[0].get("char") == "M" and right_top[0].get("char") == "S":
          found_words += 1
        elif left_top[0].get("char") == "M" and right_bottom[0].get("char") == "S" and left_bottom[0].get("char") == "S" and right_top[0].get("char") == "M":
          found_words += 1
        elif left_top[0].get("char") == "S" and right_bottom[0].get("char") == "M" and left_bottom[0].get("char") == "M" and right_top[0].get("char") == "S":
          found_words += 1
        elif left_top[0].get("char") == "S" and right_bottom[0].get("char") == "M" and left_bottom[0].get("char") == "S" and right_top[0].get("char") == "M":
          found_words += 1
      
      # if next_item and next_item[0].get("char") == to_find[1]:
      #   start_row = next_item[0].get("row")
      #   start_col = next_item[0].get("col")
        
      #   next_item = [item for item in matrix if 
      #     condition(start_row, start_col, item.get("row"), item.get("col"))]
        
      #   if next_item and next_item[0].get("char") == to_find[2]:
      #     found_words += 1
   
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
