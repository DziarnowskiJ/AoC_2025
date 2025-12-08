import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_3.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import itertools


def process(lines):
    return sum([max([int(f"{''.join([*a])}") for a in itertools.combinations(line, 2)]) for line in lines])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
# pypy ./day_03/part_1.py
