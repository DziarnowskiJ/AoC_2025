import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_5.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_5.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.lists import merge_ranges


def process(lines):
    empty = lines.index('')
    ranges = [[int(r) for r in i.split('-')] for i in lines[:empty]]

    new_ranges = merge_ranges(ranges)

    return sum([r[1] + 1 - r[0] for r in new_ranges])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_05/part_1.py
