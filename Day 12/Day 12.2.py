from aoc_utils import load_input
import math

f = load_input()

x, y = 0, 0
wx, wy = 10, 1

dirs = {
    "E": (1, 0),
    "W": (-1, 0),
    "S": (0, -1),
    "N": (0, 1)
}

def rotate(origin, point, angle):

    ox, oy = origin
    px, py = point
    angle = math.radians(angle)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

for l in f:
    inst = l[0]
    n = int(l[1:])
    
    if inst in ["R", "L"]:
        if inst == "R":
            n *= -1
        wx, wy = rotate((0, 0), (wx, wy), n)

    elif inst == "F":
        x += wx * n
        y += wy * n
    elif inst in "NSWE":
        dx, dy = dirs[inst]
        wx += dx * n
        wy += dy * n
    



print(round(abs(x) + abs(y)))