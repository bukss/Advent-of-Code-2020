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

l = set()

for bp in f:
    row = binary_search(bp[:7], 0, 127)
    col = binary_search(bp[7:], 0, 7)
    if row == 0 or row == 127:
        continue
    l.add(row*8 + col)

for i in range(max(l)):
    if i not in l and i + 1 in l and i - 1 in l:
        print(i)