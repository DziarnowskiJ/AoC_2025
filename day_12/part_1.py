import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_12.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
import re


def parse(lines):
    shps, szs = lines[:30], lines[30:]

    shapes = dict()
    while len(shps) > 0:
        idx = shps.pop(0)[:-1]
        l1 = shps.pop(0)
        l2 = shps.pop(0)
        l3 = shps.pop(0)
        shapes[idx] = (grid_dict([l1, l2, l3]), len(grid_position('#', grid_dict([l1, l2, l3]))))

        shps.pop(0)

    sizes = []
    for i in szs:
        nums = re.findall(r'\d+', i)
        x = nums.pop(0)
        y = nums.pop(0)
        sizes.append(((x, y), nums))

    return shapes, sizes


def process(lines):
    shapes, sizes = parse(lines)

    res = 0
    for line in sizes:
        size = int(line[0][0]) * int(line[0][1])
        idxs = line[1]
        fills = sum([shapes[str(i)][1] * int(c) for i, c in enumerate(idxs)])
        spaces = sum([9 * int(c) for i, c in enumerate(idxs)])

        # Check if space is large enough to fit all points (assuming 100% fit)
        if size > fills:
            # Check if all figures would fit if the figures didn't overlap
            if size < spaces:
                print('Size:', size, 'Fills:', fills, 'Spaces:', spaces)
                print('Need to cut', spaces - size, 'points')
            else:
                # Figures that can be easily arranged
                res += 1

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_12/part_1.py
