from enum import IntEnum
from typing_extensions import Self
import math


###################################################### DIRECTIONS ######################################################

# compass points
class Direction(IntEnum):
    """All possible directions in 2D space"""
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Direction.{self.name}'

    def __bool__(self):
        return True


def turn_left(direction: Direction) -> Direction:
    """Direction 90 deg to the left"""
    return Direction((direction - 2) % 8)


def turn_right(direction: Direction) -> Direction:
    """Direction 90 deg to the right"""
    return Direction((direction + 2) % 8)


def get_opposite_direction(direction: Direction) -> Direction:
    """Opposite direction"""
    return Direction((direction + 4) % 8)


######################################################## POINT #########################################################


class Point:
    """X, Y coordinates in 2D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.key = (x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self):
        return not self.__eq__(other)

    def __lt__(self, other: Self):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(self.key)

    def mul(self, n: int) -> Self:
        """Multiply both components of a point by a given number"""
        return Point(n * self.x, n * self.y)

    def norm(self) -> int:
        """Manhattan metric of the point"""
        return abs(self.x) + abs(self.y)

    def dist(self) -> float:
        """Straight-line distance from the origin"""
        return math.sqrt(self.x**2 + self.y**2)


class Origin(Point):
    """Origin in 2D space"""
    def __init__(self):
        super().__init__(0, 0)


def distance(p1: Point, p2: Point) -> int:
    """Distance between two points using the Manhattan metric"""
    return (p1 - p2).norm()


def straight_distance(p1: Point, p2: Point) -> float:
    """Straight-line distance between two points"""
    return (p1 - p2).dist()


def one_step(direction: Direction) -> Point:
    """Point one step away from the origin in the given direction"""
    steps = {
        Direction.N: Point(0, 1),
        Direction.NE: Point(1, 1),
        Direction.E: Point(1, 0),
        Direction.SE: Point(1, -1),
        Direction.S: Point(0, -1),
        Direction.SW: Point(-1, -1),
        Direction.W: Point(-1, 0),
        Direction.NW: Point(-1, 1),
    }
    return steps[direction]


def get_one_step_direction(point1: Point, point2: Point) -> Direction | None:
    """If two points are neighbouring, return direction from P1 to P2, None otherwise"""
    diff = point2 - point1

    direction_map = {
        (0, 1): Direction.N,
        (1, 1): Direction.NE,
        (1, 0): Direction.E,
        (1, -1): Direction.SE,
        (0, -1): Direction.S,
        (-1, -1): Direction.SW,
        (-1, 0): Direction.W,
        (-1, 1): Direction.NW
    }

    return direction_map.get(diff.key)


def point_neighbours(point: Point, diagonal: bool = True) -> list[Point]:
    """List of Points surrounding given point.
    Possible to include diagonal points"""
    return [point + one_step(Direction(i)) for i in Direction if diagonal or i % 2 == 0]


def are_on_same_line(point1: Point, point2: Point, diagonal=False) -> Direction or bool:
    """
    checks if two points are on the same line - horizontal or vertical.
    If diagonal = True, checks also diagonal directions

    if points are at the same location, returns True
    if they are on the same line, returns direction from p1 to p2
    if they are not on the same line, returns False

    :param point1:
    :param point2:
    :param diagonal:
    :return:
    """
    if point1.x == point2.x and point1.y == point2.y:
        return True

    dx = point2.x - point1.x
    dy = point2.y - point1.y
    if abs(dx) == abs(dy) and diagonal:
        if dx > 0 and dy > 0:
            return Direction.NE
        elif dx < 0 < dy:
            return Direction.NW
        elif dx > 0 > dy:
            return Direction.SE
        elif dx < 0 and dy < 0:
            return Direction.SW

    if point1.x == point2.x:
        return Direction.S if point1.y > point2.y else Direction.N
    if point1.y == point2.y:
        return Direction.W if point1.x > point2.x else Direction.E
    return False


######################################################### GRID #########################################################

def grid_dict_from_text(text_grid: str, origin: Direction = Direction.NE) -> dict[Point, str]:
    """Parse text into a grid"""
    lines_of_text = text_grid.split('\n')
    return grid_dict(lines_of_text, origin)


def grid_dict(grid_lines: list[str], origin: Direction = Direction.NW) -> dict[Point, str]:
    """Parse list of lines into a grid"""
    if origin == Direction.NW:
        return {Point(x, -y): c for y, line in enumerate(grid_lines)
                for x, c in enumerate(line)}
    elif origin == Direction.NE:
        return {Point(-x, -y): c for y, line in enumerate(grid_lines)
                for x, c in enumerate(reversed(line))}
    elif origin == Direction.SE:
        return {Point(-x, y): c for y, line in enumerate(reversed(grid_lines))
                for x, c in enumerate(reversed(line))}
    elif origin == Direction.SW:
        return {Point(x, y): c for y, line in enumerate(reversed(grid_lines))
                for x, c in enumerate(line)}
    else:
        raise Exception("origin can only be NE, NW, SE or SW")


def get_neighbours_dict(point: Point, grid: dict[Point, str],
                        diagonal: bool = True) -> dict[Point, str]:
    """
    Dict[Point:value] of all surrounding points if they are in a grid.
    Possible to include diagonal points
    """
    return {p: grid[p] for p in point_neighbours(point, diagonal) if is_in_grid(p, grid)}


def get_neighbours_values(point: Point, grid: dict[Point, str],
                          diagonal: bool = True) -> list[str]:
    """
    Values of all surrounding points if they are in a grid.
    Possible to include diagonal
    """
    return [v for v in get_neighbours_dict(point, grid, diagonal).values()]


def is_in_grid(point: Point, grid: dict[Point, str]) -> bool:
    """Check if point is part of the grid"""
    return point in grid.keys()


def grid_dimensions(grid: dict[Point, str]) -> tuple[Point, Point]:
    """Returns most N-W and S-E corners of the grid"""
    xs = [p.x for p in grid.keys()]
    ys = [p.y for p in grid.keys()]

    top_left = Point(min(xs), max(ys))
    bottom_right = Point(max(xs), min(ys))

    return top_left, bottom_right


def grid_position(char: str, grid: dict[Point, str]) -> list[Point]:
    """List of points with specified value"""
    return [key for key, value in grid.items() if value == char]


def points_to_text(grid: dict[Point, str]) -> str:
    """Returns string representation of the grid ready to be printed to the console"""

    # Find the maximum and minimum coordinates to determine the size of the grid
    g_bounds = grid_dimensions(grid)
    max_x = g_bounds[1].x
    min_x = g_bounds[0].x
    max_y = g_bounds[0].y
    min_y = g_bounds[1].y

    # Initialize an empty grid with spaces
    text_grid = [[' ' for _ in range(abs(max_x - min_x) + 1)] for _ in range(abs(max_y - min_y) + 1)]

    # Populate the grid with characters from the given points
    for point, char in grid.items():
        x = abs(max_x - min_x) - abs(point.x - max_x)
        y = abs(max_y - min_y) - abs(point.y - max_y)
        text_grid[y][x] = char

    # Convert the grid to a string
    text = '\n'.join(''.join(row) for row in reversed(text_grid))

    return text


def empty_grid(point1: Point, point2: Point, char: str = '.') -> dict[Point, str]:
    """Creates grid filled with given value for all points"""
    nw, se = grid_dimensions({point1: char, point2: char})
    return {Point(i, j): char
            for i in range(nw.x, se.x + 1, 1)
            for j in range(nw.y, se.y - 1, -1)}
