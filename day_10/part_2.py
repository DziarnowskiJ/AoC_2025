import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_10.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_10.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from z3 import Optimize, Int, sat, Sum
import re


def parse_line(line):
    lights = [0 if x == '.' else 1 for x in re.findall(r'\[.*]', line)[0][1:-1]]
    buttons = [tuple([int(x) for x in l]) for l in [b.split(',') for b in re.findall(r'\((\d[,\d]*)\)', line)]]
    joltage = [int(x) for x in re.findall(r'\{.*}', line)[0][1:-1].split(',')]

    return tuple(lights), tuple(buttons), tuple(joltage)


def parse(lines):
    return [parse_line(x) for x in lines]


def press(state_tuple, button_indices):
    state_list = list(state_tuple)
    for pos in button_indices:
        state_list[pos] = state_list[pos] + 1
    return tuple(state_list)


def process(lines):
    manuals = parse(lines)
    resp = 0

    for manual in manuals:
        _, buttons, joltage = manual

        button_masks = [press((0,) * len(joltage), button) for button in buttons]

        opt = Optimize()
        A_vars = [Int(f'a_{i}') for i in range(len(button_masks))]
        for jolt_pos in range(len(joltage)):
            terms = [A_vars[button_idx] * button_masks[button_idx][jolt_pos] for button_idx in range(len(button_masks))]
            opt.add(Sum(terms) == joltage[jolt_pos])

        for var in A_vars:
            opt.add(var >= 0)

        opt.minimize(Sum(A_vars))

        if opt.check() == sat:
            model = opt.model()
            min_sum = model.evaluate(Sum(A_vars))
            resp += min_sum.as_long()

    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
