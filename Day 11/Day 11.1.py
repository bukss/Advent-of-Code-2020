from aoc_utils import load_input
from copy import deepcopy

def get_adjacent_cells(y, x, grid):
    ADJ_COORDS = [
        (-1, -1), # Top left
        (-1,  0), # Top
        (-1,  1), # Top right
        ( 0,  1), # Right
        ( 1,  1), # Bottom right
        ( 1,  0), # Bottom
        ( 1, -1), # Bottom left
        ( 0, -1)  # Left
    ]
    adjacents = []

    for dy, dx in ADJ_COORDS:
        if 0 <= dy + y < len(grid) and 0 <= dx + x < len(grid[0]):
            adjacents.append(grid[dy + y][dx + x])

    return adjacents


def next_cell_state(seat, adjacents):
    if seat == "L":
        if "#" not in adjacents:
            return "#"

    if seat == "#":
        if adjacents.count("#") >= 4:
            return "L"

    return seat


def next_gen(grid):
    next_grid = deepcopy(grid)

    for y, row in enumerate(grid):
        for x, seat in enumerate(row):
            if seat == ".":
                continue

            adjacents = get_adjacent_cells(y, x, grid)
            next_grid[y][x] = next_cell_state(seat, adjacents)
    
    return next_grid


seats = [list(i) for i in load_input()]
while seats != (seats := next_gen(seats)):
    pass
   
print(sum(row.count("#") for row in seats))
