from aoc_utils import load_input

f = load_input()
n = int(f[0])
g = [int(i) for i in f[1].split(",") if i != "x"]

def get_lowest(a, target):
    n = 1
    while n * a < target:
        n += 1
    return n * a

d = {get_lowest(j, n):j for j in g}

a = min(d)
j = a-n
print(j)
print(d[a])
print(d[a]*j)

