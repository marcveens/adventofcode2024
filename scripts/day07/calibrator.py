from get_file import get_file_contents

def calibrate(file_name):
  contents = get_file_contents(file_name)
  
  sum = 0

  for key in contents.keys():
   if has_solution(key, contents[key]):
     sum += key
    
  return sum
    
def has_solution(total, values):
  def recursive(start, end):
    if start == end:
        return {values[start]}
      
    outcomes = set()
    
    # Try all possible splits
    for i in range(start, end):
        left_results = recursive(start, i)
        right_results = recursive(i + 1, end)
        
        # Combine results using + and *
        for left in left_results:
            for right in right_results:
                outcomes.add(left + right)  # Add combination
                outcomes.add(left * right)  # Multiply combination
    
    return outcomes
    
  solutions = recursive(0, len(values) - 1)
  
  return total in solutions