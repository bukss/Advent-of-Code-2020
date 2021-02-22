from aoc_utils import load_input
import re
from collections import defaultdict

f = load_input()

for i, l in enumerate(f):
    l = re.sub(r"([sn][ew])", r" \1 ", l)
    l = re.sub(r"(?<![ns])([ew])", r" \1 ", l)
    f[i] = list(filter(bool, l.split()))

flips = defaultdict(bool)

for l in f:
    x, y, z = 0, 0, 0
    for d in l:
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
        
    coords = (x, y, z)
    flips[coords] = not flips[coords]

print(sum(flips.values()))