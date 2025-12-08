import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_2.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.text_funcs import split_string


def process(lines):
    ids = lines[0].split(',')
    res = 0
    for ranges in ids:
        start, end = [int(r) for r in ranges.split('-')]

        for val in range(start, end + 1):
            splits = split_string(str(val))
            for spl in splits:
                # if all splits are the same, set will have length 1
                if len(set(spl)) == 1 and len(spl) != 1:
                    res += val
                    break

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
# pypy ./day_02/part_2.py
