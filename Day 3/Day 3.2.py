from aoc_utils import load_input

trees = load_input()

def get_trees(dx, dy):
    x, y = 0, 0
    t = 0
    while y < len(trees):
        if trees[y][x] == "#":
            t += 1
        x = (x + dx) % len(trees[y])
        y += dy
    return t

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
)
r = 1
for s in slopes:
    r *= get_trees(*s)


print(r)