import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_10.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_10.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re
from collections import deque


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
        state_list[pos] = 1 - state_list[pos]
    return tuple(state_list)


def process(lines):
    manuals = parse(lines)
    resp = 0

    for manual in manuals:
        target_state, buttons, _ = manual
        state_length = len(target_state)

        queue = deque([((0,) * state_length, 0)])  # (current_state, steps)
        visited = {((0,) * state_length)}

        min_steps = 0
        while queue:
            current_state, steps = queue.popleft()

            # Check if reached the target state
            if current_state == target_state:
                min_steps = steps
                break

            # Create possible states by pressing each button combination
            for button in buttons:
                next_state = press(current_state, button)

                # Add unseen steps to queue
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))

        resp += min_steps

    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
