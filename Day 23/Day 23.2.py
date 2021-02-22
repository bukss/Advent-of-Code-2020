from aoc_utils import load_raw

f = list(map(int, list(load_raw()))) + list(range(10, 1_000_001))
size = len(f)
cups = {f[i]:f[(i+1)%size] for i in range(size)}

current = f[0]

min_cup, max_cup = min(cups), max(cups)
n = 10_000_000
counter = 0
for i in range(n):
    first = cups[current]
    second = cups[first]
    third = cups[second]
    destination = current - 1

    while 1:
        if destination < min_cup:
            destination = max_cup
        if destination != first and destination != second and destination != third:
            break
        destination -= 1

    next_current = cups[third]
    cups[third] = cups[destination]
    cups[current] = next_current
    cups[destination] = first
    current = next_current

a = cups[1]
b = cups[a]

print(a, b)
print(a*b)