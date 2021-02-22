from aoc_utils import load_input
from tile_class import Tile
from collections import defaultdict

f = load_input("\n\n")

tiles = []
for t in f:
    n = int(t.split()[1][:-1])
    p = t.splitlines()[1:]
    tiles.append(Tile(n, p))

#print([]

edges = defaultdict(list)

for tile in tiles:
    for edge in tile.edges:
        edges[edge].append(tile)
        edges[edge[::-1]].append(tile)

found = []

for e, t in edges.items():
    if len(t) == 2:
        t1, t2 = t
        t1.adj[e], t2.adj[e] = t2, t1
        found.append(e)

for e in found:
    del edges[e]

print(tiles[0].adj)
c = 1
for t in tiles:
    if len(t.adj) == 4:
        c *= t.number

print(c)