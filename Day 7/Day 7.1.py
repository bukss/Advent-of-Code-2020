from aoc_utils import load_input
from collections import defaultdict
import re

f = load_input()

bags = defaultdict(set)
for l in f:
    if "no other bags" in l:
        continue
    container = re.match(r"(\b.*) bags contain", l).groups()[0]
    colors = re.findall(r"[0-9] (.+?) bag", l)
    bags[container] = set(colors)


def contains(c):
    s = set()
    for color in bags[c]:
        s.add(color)
        if color not in bags:
            continue
        s.update(contains(color))

    return s

print(len([i for i in bags if "shiny gold" in contains(i)]))