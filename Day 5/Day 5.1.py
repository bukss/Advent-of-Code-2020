from aoc_utils import load_input
from math import ceil, floor

f = load_input()

def binary_search(s, min, max):
    r_min = min
    r_max = max
    for c in s:
        if c == "F" or c == "L":
            r_max = r_min + ceil((r_max - r_min)/2)
        elif c == "B" or c == "R":
            r_min = r_max - floor((r_max - r_min)/2)
    return r_min

l = []

for bp in f:
    row = binary_search(bp[:7], 0, 127)
    col = binary_search(bp[7:], 0, 7)
    l.append(row*8 + col)

print(max(l))