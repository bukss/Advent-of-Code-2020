from aoc_utils import load_input
from math import atan, sin, cos, radians

f = load_input()

x, y = 0, 0

facing = 0

dirs = {
    "E": (1, 0),
    "W": (-1, 0),
    "S": (0, -1),
    "N": (0, 1)
}

for l in f:
    inst = l[0]
    n = int(l[1:])
    dx, dy = cos(radians(facing)), sin(radians(facing))
    if 90 < facing < 270:
        dx = -1 * abs(dx)
    if 180 < facing < 360:
        dy = -1 * abs(dy)
    if inst in ["R", "L"]:
        if inst == "R":
            facing -= n
        else:
            facing += n
    elif inst == "F":
        x += dx * n
        y += dy * n
    elif inst in "NSWE":
        dx, dy = dirs[inst]
        x += dx * n
        y += dy * n

print(x, y)
print(round(abs(x) + abs(y)))