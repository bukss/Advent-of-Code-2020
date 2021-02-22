from aoc_utils import load_input
import re

f = load_input("\n\n")
tags = f[0].splitlines()
tag_info = {}
flat_ranges = []
for tag in tags:
    t_parts = tag.split(": ")
    name = t_parts[0]
    nums = t_parts[1].split(" or ")
    ranges = [tuple(int(j) for j in i.split("-")) for i in nums]
    tag_info[name] = ranges
    flat_ranges.extend(ranges)

tickets = [list(map(int, i.split(","))) for i in f[2].splitlines()[1:]]
c = 0

def validate_ticket(ticket):
    invalid = 0
    for n in ticket:
        if not any(a <= n <= b for a, b in flat_ranges):
            invalid += n
            print(n)
    return invalid
print(sum(validate_ticket(ticket) for ticket in tickets))