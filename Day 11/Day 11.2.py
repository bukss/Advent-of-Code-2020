from aoc_utils import load_input
from copy import deepcopy

def get_visible_cells(y, x, grid):
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
    visibles = []

    for dy, dx in ADJ_COORDS:
        dist = 1
        while (0 <= y + dist*dy < len(grid)) and (0 <=  x + dist*dx < len(grid[0])):
            newy = y + dist*dy
            newx = x + dist*dx
            if grid[newy][newx] != ".":
                visibles.append(grid[newy][newx])
                break
            dist += 1

    return visibles


def next_cell_state(seat, visibles):
    if seat == "L":
        if "#" not in visibles:
            return "#"

    if seat == "#":
        if visibles.count("#") >= 5:
            return "L"
    
    return seat


def next_gen(grid):
    next_grid = deepcopy(grid)

    for y, row in enumerate(grid):
        for x, seat in enumerate(row):
            if seat == ".":
                continue

            visibles = get_visible_cells(y, x, grid)
            next_grid[y][x] = next_cell_state(seat, visibles)

    return next_grid
    

seats = [list(i) for i in load_input()]
while seats != (seats := next_gen(seats)):
    pass
   
print(sum(row.count("#") for row in seats))
