import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.search import paths_count


def parse(lines):
    return {f: tuple(to.split()) for f, to in [line.split(':') for line in lines]}


def process(lines):
    conns = parse(lines)

    return paths_count('you', 'out', conns)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_11/part_1.py
