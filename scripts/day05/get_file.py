import os

def get_file_contents(fileName):
  script_dir = os.path.dirname(os.path.abspath(__file__))

  file = open(os.path.join(script_dir, fileName), 'r')
  content = file.read()
  
  split_content = content.split("\n\n")
  
  rules_input = split_content[0].split("\n")
  rules = [list(map(int, item.split('|'))) for item in rules_input]
  
  pages_input = split_content[1].split("\n")
  pages = [list(map(int, item.split(","))) for item in pages_input]
  
  return {
    "rules": rules,
    "pages": pages
  }
