import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_4.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_4.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]
  
from utils.geometry import *
  
    
def process(lines):
    res = 0
    grid = grid_dict(lines)
    points = grid_position('@', grid)
    for point in points:
        adj = get_neighbours_values(point, grid)
        if len([x for x in adj if x == '@']) < 4:
            res += 1
    return res

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_04/part_1.py
