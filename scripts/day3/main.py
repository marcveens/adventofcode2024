import os

from get_mul_instructions import get_mul_instructions

script_dir = os.path.dirname(os.path.abspath(__file__))

file = open(os.path.join(script_dir, 'input.txt'), 'r')
content = file.read()

results = get_mul_instructions(content)
outcome = 0

for item in results:
    outcome += item.get("outcome")
    
print(outcome)