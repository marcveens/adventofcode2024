from get_file import get_file_contents

def validate_manual(file_name):
  contents = get_file_contents(file_name)
  
  rules = contents.get("rules")
  pages = contents.get("pages")
  
  sum = 0
  
  for page in pages:
    is_valid = validate_page(page, rules)
    
    # if is_valid:
      # sum += page[len(page)//2]
  
    if not is_valid:
      new_page = page
      print(f"before {page}")
      while not validate_page(page, rules):
        new_page = fix_page(new_page, rules)
        print(f"fix: {new_page}")
        
      sum += new_page[len(new_page)//2]
      
  return sum

     
def validate_page(page, rules):
  for rule in rules:
    first = rule[0]
    second = rule[1]
    
    first_index = page.index(first) if first in page else -1
    second_index = page.index(second) if second in page else -1
    
    if first_index > -1 and second_index > -1:
      if second_index < first_index:
        return False
      
  return True

def fix_page(page, rules):
  for rule in rules:
    first = rule[0]
    second = rule[1]
    
    first_index = page.index(first) if first in page else -1
    second_index = page.index(second) if second in page else -1
    
    if first_index > -1 and second_index > -1:
      if second_index < first_index:
        # Put number 1 in front of number 2
        page.pop(first_index)
        
        page.insert(second_index, first)
        
  return page