from aoc_utils import load_input
from tile_class import Tile, DIR_COORDS
from collections import defaultdict
from math import sqrt

f = load_input("\n\n")




picture = {}
def dfs(tile, x, y):
    picture[tile] = (x, y)
    for d, t in tile.adj_tiles.items():
        if t in picture:
            continue
        dx, dy = DIR_COORDS[d]
        dfs(t, x+dx, y+dy)


tiles = []
for t in f:
    n = int(t.split()[1][:-1])
    p = t.splitlines()[1:]
    tiles.append(Tile(n, p))

edges = defaultdict(list)

for tile in tiles:
    for edge in tile.edges.values():
        edges[edge].append(tile)
        edges[edge[::-1]].append(tile)

found = []

for e, t in edges.items():
    if len(t) == 2:
        t1, t2 = t
        t1.adj_edges[e], t2.adj_edges[e] = t2, t1
        found.append(e)

SEA_MONSTER = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "
]

def flip(p):
    return p[::-1]

def rotate(p):
    return list(zip(*p[::-1]))

def find_sea_monsters(p):
    smc = [[(x, y) for x, c in enumerate(row) if c == "#"] for y, row in enumerate(SEA_MONSTER)]
    sea_monster_coords = []
    for row in smc:
        [sea_monster_coords.append(coord) for coord in row]
    counter = 0
    for y in range(len(p)-3):
        for x in range(len(p[0]) - len(SEA_MONSTER[0])):
            if all(p[y+dy][x+dx] == "#" for dx, dy in sea_monster_coords):
                counter += 1
    
    return counter

tiles[0].oriented = True
tiles[0].orient(None)
tile_size = len(tiles[0].pattern)-2
for tile in tiles:
    tile.pattern = [row[1:-1] for row in tile.pattern[1:-1]]

dfs(tiles[0], 0, 0)
size = int(sqrt(len(tiles)))
connected = [[None]*size for i in range(size)]
corner_x_offset = min([i[0] for i in picture.values()])
corner_y_offset = min([i[1] for i in picture.values()])
for t, c in picture.items():
    x, y = c[0]-corner_x_offset, c[1]-corner_y_offset
    connected[y][x] = ["".join(r) for r in t.pattern][::-1]


connected = list(zip(*connected[::-1]))
connected = list(zip(*connected[::-1]))

picture_ = []
for tile_row in connected:
    big_row = []
    for i in range(tile_size):
        small_row = "".join([tile[i] for tile in tile_row])
        big_row.append(small_row)
    picture_.append(big_row)

picture = []
for big_row in picture_:
    for row in big_row:
        picture.append(row)

for row in picture:
    row = "".join("".join(row))

brackishness = ("\n".join(picture)).count("#")

smc_counts = []
for i in range(4):
    picture = rotate(picture)
    smc_counts.append(find_sea_monsters(picture))
    picture = flip(picture)
    smc_counts.append(find_sea_monsters(picture))
    picture = flip(picture)

sea_monster_count = max(smc_counts)
sea_monster_mass = ("\n".join(SEA_MONSTER)).count("#")


roughness = brackishness - (sea_monster_mass*sea_monster_count)
print(roughness)