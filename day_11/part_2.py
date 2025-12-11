import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from functools import lru_cache


def parse(lines):
    return {f: tuple(to.split()) for f, to in [line.split(':') for line in lines]}


def paths_count(start, end, conns):
    @lru_cache(maxsize=None)
    def _path_count(curr, target, fft, dac):
        if curr == target:
            return 1 if fft and dac else 0
        return sum(_path_count(n, target, n == 'fft' or fft, n == 'dac' or dac) for n in conns[curr])

    _path_count.cache_clear()
    return _path_count(start, end, False, False)


def process(lines):
    conns = parse(lines)

    return paths_count('svr', 'out', conns)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_11/part_1.py
