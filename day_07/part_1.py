import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_7.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *


def process(lines):
    grid = grid_dict(lines)
    start = grid_position('S', grid)[0]

    check_points = [start]
    counter = 0
    while len(check_points) > 0:
        point = check_points.pop(0)
        below = point + one_step(Direction.S)
        if not is_in_grid(below, grid):
            break
        if grid[below] == '^':
            counter += 1
            check_points.append(below + one_step(Direction.W))
            grid[below + one_step(Direction.W)] = '|'
            check_points.append(below + one_step(Direction.E))
            grid[below + one_step(Direction.E)] = '|'
        elif grid[below] == '.':
            check_points.append(below)
            grid[below] = '|'

    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_07/part_1.py
