import platform
import math

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_1.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    pos = 50
    res = 0

    for point in lines:
        old_pos = pos
        dir_point = point[0]
        val_point = eval(point.replace('R', '+').replace('L', '-'))
        pos = (pos + val_point) % 100

        if old_pos == 0:
            # Don't double count 0 from previous iteration
            pass
        elif pos == 0:
            # Stopped at 0
            res += 1
        elif old_pos > pos and dir_point == 'R':
            # Went past 0 right
            res += 1
        elif old_pos < pos and dir_point == 'L':
            # Went past 0 left
            res += 1

        res += math.floor(abs(val_point) / 100)

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_01/part_2.py
