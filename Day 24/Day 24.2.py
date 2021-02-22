from aoc_utils import load_input
import re
from collections import defaultdict

f = load_input()

for i, l in enumerate(f):
    l = re.sub(r"([sn][ew])", r" \1 ", l)
    l = re.sub(r"(?<![ns])([ew])", r" \1 ", l)
    f[i] = list(filter(bool, l.split()))

tiles = defaultdict(bool)

DIRS = ("nw", "ne", "se", "sw", "e", "w")

def get_adj_tile(coord, d):
    x, y, z = coord
    if d == "nw":
        y += 1
        z -= 1
    elif d == "se":
        y -= 1
        z += 1

    elif d == "ne":
        x += 1
        z -= 1
    elif d == "sw":
        x -= 1
        z += 1

    elif d == "e":
        x += 1
        y -= 1

    elif d == "w":
        x -= 1
        y += 1
    
    return (x, y, z)

for l in f:
    coords = (0, 0, 0)
    for d in l:
        coords = get_adj_tile(coords, d)
    tiles[coords] = not tiles[coords]

print(f"0: {sum(tiles.values())}")
for i in range(100):
    white_tile_neighbors = defaultdict(int)
    new_flip = []
    for tile, tile_state in list(tiles.items()):
        adj = [get_adj_tile(tile, d) for d in DIRS]
        black_adj = sum(map(bool, map(tiles.get, adj)))

        for coord in adj:
            if (coord not in tiles) and tile_state:
                white_tile_neighbors[coord] += 1

        if (not tile_state) and (black_adj == 2):
            new_flip.append(tile)

        if tile_state and (black_adj == 0 or black_adj > 2):
            new_flip.append(tile)

    for tile, count in white_tile_neighbors.items():
        if count == 2:
            new_flip.append(tile)

    for tile in new_flip:
        tiles[tile] = not tiles[tile]        
    print(f"{i+1}: {sum(tiles.values())}")

print(sum(tiles.values()))