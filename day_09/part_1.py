import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
from itertools import combinations


def process(lines):
    points = [Point(int(x), int(y)) for line in lines
              for (x, y) in [line.split(',')]]

    conns = [((abs((x[0] - x[1]).x + 1) * ((x[0] - x[1]).y + 1)), x) for x in
             [p for p in list(combinations(points, 2))]]
    conns.sort(key=lambda x: x[0], reverse=True)

    return conns[0][0]


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_09/part_1.py
