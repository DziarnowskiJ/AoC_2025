import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_6.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from functools import reduce
from operator import mul


def process(lines):
    # extract operators and append values
    eqs = dict()
    for line in reversed(lines):
        for i, nums in enumerate(line.split()):
            if i in eqs:
                eqs[i].append(int(nums))
            else:
                eqs[i] = [nums]

    # perform operations and sum values
    resp = 0
    for val in eqs.values():
        if val[0] == '*':
            resp += reduce(mul, val[1:])
        else:
            resp += sum(val[1:])
    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_06/part_1.py
