import os

def get_file_contents(file_name):
  script_dir = os.path.dirname(os.path.abspath(__file__))

  file = open(os.path.join(script_dir, file_name), 'r')
  content = file.read()
  
  split_content = content.split("\n")
  
  map = {}
  
  for item in split_content:
    split_item = item.split(": ")
    
    map[int(split_item[0])] = [int(item) for item in split_item[1].split(" ")]
  
  return map
