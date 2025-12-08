import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_7.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
from functools import lru_cache


@lru_cache()
def check_below(point):
    below = point[0] + one_step(Direction.S)
    orig = point[1]
    if not is_in_grid(below, grid):
        return 0
    if grid[below] == '^':
        return (check_below((below + one_step(Direction.W), 0)) +
                check_below((below + one_step(Direction.E), 1)))
    else:
        return orig + check_below((below, 0))


def process(lines):
    global grid
    grid = grid_dict(lines)
    start = grid_position('S', grid)[0]

    return check_below((start, 1))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_07/part_1.py
