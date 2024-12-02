def is_list_safe(list):
  is_safe = True
  last_item = None
  
  order_decided = False
  is_increasing = False
  is_decreasing = False
  
  for item in list:
    if last_item == None:
      last_item = item
      continue
    
    if item > last_item:
      is_increasing = True
      order_decided = True
    elif item < last_item:
      is_decreasing = True
      order_decided = True
      
    if order_decided == False:
      return False
      
    if is_increasing == True:
      if item < last_item or item == last_item:
        is_safe = False
        
      difference = item - last_item
      
      if difference > 3:
        is_safe = False
        
    if is_decreasing == True:
      if item > last_item or item == last_item:
        is_safe = False
        
      difference = last_item - item
      
      if difference > 3:
        is_safe = False
    
    last_item = item
  
  return is_safe