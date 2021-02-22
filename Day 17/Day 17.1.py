from aoc_utils import load_input
from itertools import product
import numpy as np
from collections import Counter

cube = np.array([[list(s) for s in load_input()]])

c = set(product((0, 1, -1), (0, 1, -1), (0, 1, -1)))
c.remove((0, 0, 0))
ADJ_COORDS = c


def get_active_neighbors(x, y, z):
    active = 0
    for dy, dx, dz in ADJ_COORDS:
        ny, nx, nz = new_coords = (y+dy, x+dx, z+dz)

        if any(i < 0 for i in new_coords):
            continue

        try:
            if cube[nz][ny][nx] == "#":
                active += 1
        except IndexError:
            continue

    return active

for i in range(6):
    cube = np.pad(cube, ((1, 1), (1, 1), (1, 1)), mode="constant", constant_values=".")

    print(i)
    change = {"#": set(), ".": set()}
    for z, layer in enumerate(cube):
        for y, row in enumerate(layer):
            for x, cell in enumerate(row):
                neighbors = get_active_neighbors(x, y, z)

                if cell == "#":
                    if neighbors != 2 and neighbors != 3:
                        change["."].add((z, y, x))
                else:
                    if neighbors == 3:
                        change["#"].add((z, y, x))

    for state, coords in change.items():
        for z, y, x in coords:
            cube[z][y][x] = state

flat = list(cube.flatten())
print(flat.count("#"))