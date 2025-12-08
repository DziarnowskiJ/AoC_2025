import platform
import math

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_2.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    ids = lines[0].split(',')
    res = 0
    for ranges in ids:
        start, end = [int(r) for r in ranges.split('-')]

        for val in range(start, end + 1):
            val_str = str(val)
            val_len = len(val_str) // 2

            if val_str[:val_len] == val_str[val_len:]:
                res += val

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_02/part_1.py
