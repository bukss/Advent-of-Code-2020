from aoc_utils import load_input
from collections import defaultdict
import re

f = load_input()

bags = defaultdict(dict)
for l in f:
    if "no other bags" in l:
        continue
    container = re.match(r"(\b.*) bags contain", l).group(0)
    for color in re.findall(r"([0-9]+?) (.+?) bag", l):
        bags[container][color[1]] = int(color[0])

def contents(c, total = 0):
    i = total
    for color in bags[c]:
        n = bags[c][color]
        if color in bags:
            i += n * contents(color, total)
        i += n
        
    return i

print(contents("shiny gold"))