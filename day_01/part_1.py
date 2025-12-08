import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_1.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    pos = 50
    res = 0
    for point in lines:
        point = eval(point.replace('R', '+').replace('L', '-'))
        pos = pos + point
        if pos % 100 == 0:
            res += 1

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_01/part_1.py
