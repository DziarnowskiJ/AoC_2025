import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_6.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from functools import reduce
from operator import mul


def can_be_cast(val):
    try:
        x = int(val)
        return x
    except Exception as e:
        return False


def process(lines):
    # get operators in order
    eqs = [[line] for line in lines[-1].split()]

    # extract numbers vertically
    numbers = [[i for i in line] for line in lines]
    vals = []
    for i in range(len(numbers[0])):
        val = ''
        for j in range(len(numbers) - 1):
            try:
                val += numbers[j][i]
            except Exception as e:
                pass
        vals.append(val.strip())
    vals.append('')

    # append numbers to corresponding operations
    for eq in eqs:
        val = can_be_cast(vals.pop(0))
        while val:
            eq.append(val)
            val = can_be_cast(vals.pop(0))

    # perform operations and sum values
    resp = 0
    for eq in eqs:
        if eq[0] == '*':
            resp += reduce(mul, eq[1:])
        else:
            resp += sum(eq[1:])

    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_06/part_1.py
