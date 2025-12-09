import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
from functools import lru_cache
from collections import deque


def generate_grid_lookup(grid_keys):
    """For faster computation and caching capabilities, create global horizontal and vertical lookups for the gird"""
    global x_map, y_map
    x_map, y_map = {}, {}

    for p in grid_keys:
        # Build X Map (stores Ys for a fixed X)
        if p.x not in x_map:
            x_map[p.x] = []
        x_map[p.x].append(p.y)

        # Build Y Map (stores Xs for a fixed Y)
        if p.y not in y_map:
            y_map[p.y] = []
        y_map[p.y].append(p.x)

    for x in x_map:
        x_map[x].sort()
    for y in y_map:
        y_map[y].sort()

    return x_map, y_map


@lru_cache()
def get_inner(point):
    """Return all diagonal neighbours of the point that are within created polygon"""
    neighbours = [point + one_step(d) for d in [Direction.NW, Direction.NE, Direction.SE, Direction.SW]]
    fills = set()
    for n in neighbours:
        # x points
        xs = x_map.get(n.x, [])
        count_above = sum(1 for y in xs if y > n.y)
        yfill = count_above % 2 == 1

        # y points
        ys = y_map.get(n.y, [])
        count_left = sum(1 for x in ys if x < n.x)
        xfill = count_left % 2 == 1

        if yfill and xfill:
            fills.add(n)

    return tuple(fills)


def get_point_area(p1, p2):
    return (abs(p1.x - p2.x) + 1) * ((abs(p1.y - p2.y)) + 1)


@lru_cache()
def is_within_points(p1, p2, grid_points):
    """Check if any of the points are within area bounded by p1 and p2"""
    minx = min(p1.x, p2.x)
    maxx = max(p1.x, p2.x)
    miny = min(p1.y, p2.y)
    maxy = max(p1.y, p2.y)

    generator = (k for k in grid_points
                 if minx < k.x < maxx and miny < k.y < maxy)
    inside_point = next(generator, None)
    return inside_point is not None


def qualify(p1, p2, grid_keys):
    # There are no points in the grid that would fall within the area between two points
    # (this is to ensure area is full)
    no_inner = not is_within_points(p1, p2, grid_keys)

    # Check if the area is within created polygon
    insides = get_inner(p1)
    is_area_inner = is_within_points(p1, p2, insides)

    return no_inner and is_area_inner


def process(lines):
    points = [Point(int(x), -int(y)) for line in lines
              for (x, y) in [line.split(',')]]
    grid = {p: '#' for p in points}

    # connect points on the grid
    grid_points = deque(points)
    fp = grid_points[0]
    p = grid_points.popleft()
    while len(grid_points) > 0:
        n = grid_points.popleft()
        d = are_on_same_line(p, n)
        while isinstance(d, Direction):
            p = p + one_step(d)
            grid[p] = 'X'
            d = are_on_same_line(p, n)
        grid[n] = '#'
    d = are_on_same_line(n, fp)
    while isinstance(d, Direction):
        n = n + one_step(d)
        grid[n] = 'X'
        d = are_on_same_line(n, fp)
    grid[n] = '#'

    # create grid lookup for faster horizontal-vertical searches
    grid_keys = tuple([k for k in grid.keys()])
    generate_grid_lookup(grid)

    # Largest area found
    largest_so_far = (0, 0, None, None)

    # Iterate through all points
    queue = deque(points)
    i = 0
    while len(queue) > 0:
        p = queue.popleft()
        # To avoid heavy computation (finding the largest area inside the grid)
        # start checks with points creating the largest overall area
        # and find the first one that qualifies
        areas = [((p - n).get_area(), p, n) for n in queue if n.x != p.x and n.y != p.y]
        areas.sort(key=lambda x: x[0], reverse=True)
        largest_area = ((get_point_area(p, n), a, p, n)
                        for a, p, n in areas
                        if a > largest_so_far[1]
                        and qualify(p, n, grid_keys))
        res = next(largest_area, (0, 0, 0, 0))

        # If area is larger than seen so far, keep it
        if res[0] > largest_so_far[0]:
            largest_so_far = res

        if i % 10 == 0 and i != 0:
            print(f'Got through {i} points so far')
        i += 1

    return largest_so_far[0]


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_09/part_2.py
