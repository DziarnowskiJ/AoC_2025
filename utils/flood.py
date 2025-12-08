from collections import deque
from utils.geometry import *


def flood_fill(grid: dict[Point, str], start_point: Point, fill_char: str, diagonal=False) -> dict[Point, str]:
    """
    Perform flood fill on a grid starting from the given point.

    Parameters:
    - grid: A dictionary representing the grid.
    - start_point: The starting point for the flood fill.
    - fill_char: The character to fill the connected region with.
    - diagonal: allow diagonal connection

    Returns:
    A new grid with the flooded area filled with the specified character.
    """

    # Check if the starting point is in the grid
    if not is_in_grid(start_point, grid):
        raise ValueError("Starting point is outside the grid.")

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Initialize the queue for BFS
    queue = deque([start_point])

    # Keep track of visited points
    visited = set()

    # Perform BFS until the queue is empty
    while queue:
        current_point = queue.popleft()

        # Check if the current point is within the grid and has not been visited
        if is_in_grid(current_point, new_grid) and current_point not in visited:
            # Fill the current point with the new character
            new_grid[current_point] = fill_char

            # Mark the current point as visited
            visited.add(current_point)

            # Add neighbors to the queue
            neighbors = get_neighbours_dict(current_point, new_grid, diagonal=diagonal)
            queue.extend(neighbors)

    return new_grid
