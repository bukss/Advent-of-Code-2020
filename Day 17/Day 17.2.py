from aoc_utils import load_input
from itertools import product
import numpy as np
from collections import Counter

hypercube = np.array([[[list(s) for s in load_input()]]])
DIM = ((1, 1), (1, 1), (1, 1), (1, 1))

c = set(product(*((0, 1, -1),)*4)) - set(((0, 0, 0, 0),))
ADJ_COORDS = c


def get_active_neighbors(w, z, y, x):
    active = 0
    for dw, dz, dy, dx in ADJ_COORDS:
        nw, nz, ny, nx = new_coords = (w+dw, z+dz, y+dy, x+dx)
        if any(i < 0 for i in new_coords):
            continue

        try:
            if hypercube[nw][nz][ny][nx] == "#":
                active += 1
        except IndexError:
            continue
    
    return active

for i in range(6):
    hypercube = np.pad(hypercube, DIM, mode="constant", constant_values=".")

    print(i)
    print("{}x{}x{}x{}".format(*hypercube.shape))
    change = {"#": set(), ".": set()}
    for w, cube in enumerate(hypercube):
        for z, layer in enumerate(cube):
            for y, row in enumerate(layer):
                for x, cell in enumerate(row):
                    coords = (w, z, y, x)
                    neighbors = get_active_neighbors(*coords)
                    
                    if cell == "#":
                        if neighbors != 2 and neighbors != 3:
                            change["."].add(coords)
                    else:
                        if neighbors == 3:
                            change["#"].add(coords)

    for state, coords in change.items():
        for w, z, y, x in coords:
            hypercube[w][z][y][x] = state

flat = list(hypercube.flatten())
print(flat.count("#"))