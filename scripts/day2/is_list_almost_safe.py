def is_list_almost_safe(list):
  is_safe = False

  is_almost_safe = check_list(list)
  
  if is_almost_safe:
    is_safe = True
  else:
    for index_to_remove in range(len(list)):
      modified_list = [val for idx, val in enumerate(list) if idx != index_to_remove]
      
      if check_list(modified_list):
        is_safe = True

  return is_safe
    

def check_list(list):
  last_item = None
  is_safe = True
  
  is_increasing = is_list_mostly_increasing(list)
  is_decreasing = not is_list_mostly_increasing(list)
  
  for item in list:
    if last_item == None:
      last_item = item
      continue
    
    if is_increasing == True:
      if item < last_item or item == last_item:
        is_safe = False
        
      else:
        difference = item - last_item
        
        if difference > 3 or difference < 1: 
            is_safe = False
        
    elif is_decreasing == True:
      if item > last_item or item == last_item:
        is_safe = False
      
      else:
        difference = last_item - item
        
        if difference > 3 or difference < 1:
            is_safe = False
    
    last_item = item
    
  return is_safe


def is_list_mostly_increasing(list):  
  last_item = None
  increase_count = 0
  decrease_count = 0
  
  for item in list:
    if last_item == None:
      last_item = item
      continue
    
    if last_item > item:
      decrease_count += 1
    elif last_item < item:
      increase_count += 1
  
    last_item = item
    
  return increase_count > decrease_count
