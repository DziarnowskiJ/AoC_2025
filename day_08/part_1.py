import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_8.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_8.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry3D import Point, straight_distance
from itertools import combinations
from functools import reduce
from operator import mul


def process(lines, conns_count):
    points = [Point(int(x), int(y), int(z))
              for line in lines
              for x, y, z in [line.split(',')]]

    # All possible combinations, sorted based on distance
    conns = [(straight_distance(p[0], p[1]), p[0], p[1]) for p in combinations(points, 2)]
    conns.sort(key=lambda x: x[0])

    # Dict to store point groups
    groups = dict()
    # Index for groups dict
    max_ind = 0

    # Set of already used points
    used = set()

    # Run for X connections
    for i in range(conns_count):
        dist, p1, p2 = conns.pop(0)
        # No points used yet - create new group
        if p1 not in used and p2 not in used:
            groups[max_ind] = {p1, p2}
            max_ind += 1
            used.add(p1)
            used.add(p2)
        # P1 already used -> add P2 to P1's group
        elif p1 in used and p2 not in used:
            for k, v in groups.items():
                if p1 in v:
                    groups[k].add(p2)
                    used.add(p2)
        # P2 already used -> add P1 to P2's group
        elif p1 not in used and p2 in used:
            for k, v in groups.items():
                if p2 in v:
                    groups[k].add(p1)
                    used.add(p1)
        # Both points already used -> combine both groups
        elif p1 in used and p2 in used:
            p1u = [k for k, v in groups.items() if p1 in v][0]
            p2u = [k for k, v in groups.items() if p2 in v][0]
            if p1u != p2u:
                groups[p1u].update(groups[p2u])
                del groups[p2u]

    # Sorted list of connections lengths
    vals = [len(v) for v in groups.values()]
    vals.sort(reverse=True)

    return reduce(mul, vals[:3])


print("Sample output:", process(sample_lines, 10))
print("Answer:", process(input_lines, 1000))

# pypy ./day_08/part_1.py
