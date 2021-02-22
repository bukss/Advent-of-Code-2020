from aoc_utils import load_input
from bad_math import euclid, remainder_theorem

f = load_input()[1].split(",")
buses = {}

for i, n in enumerate(f):
    if n != "x":
        n = int(n)
        buses[n] = -1 * i

buses = list(buses.items())

while len(buses) > 1:
    print(buses)
    n1, a1 = buses[0]
    n2, a2 = buses[1]
    result = remainder_theorem(a1, n1, a2, n2)
    buses[:2] = [(n1*n2, result)]

print(buses[0][1])

