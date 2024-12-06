import os

def get_file_contents(file_name):
  script_dir = os.path.dirname(os.path.abspath(__file__))

  file = open(os.path.join(script_dir, file_name), 'r')
  content = file.read()
  
  return content
