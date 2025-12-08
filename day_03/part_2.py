import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_3.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    res = 0
    for line in lines:
        vals = [int(v) for v in line]

        charge = ''
        while len(charge) < 12:
            # End index of the search - ensure there's enough vals to complete
            required_len = len(charge) - 11
            end_inx = None if required_len == 0 else required_len

            # Max val in list
            max_val = max(vals[:end_inx])
            inx = vals.index(max_val)
            # Truncate list after pulling out value
            vals = vals[inx+1:]

            charge += str(max_val)
        res += int(charge)

    return res


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
# pypy ./day_03/part_2.py
