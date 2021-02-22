from aoc_utils import load_raw

f = list(map(int, list(load_raw())))
size = len(f)
cups = {f[i]:f[(i+1)%size] for i in range(size)}

min_cup, max_cup = min(f), max(f)
current = f[0]

n = 100

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

k = cups[1]
s = ""
while k != 1:
    s += str(k)
    k = cups[k]

print(s)