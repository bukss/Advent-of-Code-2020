from aoc_utils import load_input
from collections import defaultdict

f = load_input("\n\n")
TAGS = f[0].splitlines()
TICKET = f[1].splitlines()[1].split(",")
NEAR_TICKETS = [list(map(int, i.split(","))) for i in f[2].splitlines()[1:]]

tag_info = {}

for tag in TAGS:
    t_parts = tag.split(": ")
    name = t_parts[0]
    nums = t_parts[1].split(" or ")
    tag_info[name] = [tuple(int(j) for j in i.split("-")) for i in nums]

all_fields = set(tag_info.keys())

def get_valid_fields(n):
    valid = set()
    for k, v in tag_info.items():
        if any(a <= n <= b for a,b in v):
            valid.add(k)

    return valid

def remove_all(fields, tag, index):
    for k in fields:
        if tag in fields[k] and k != index:
            fields[k].remove(tag)

fields = defaultdict(list)

for ticket in NEAR_TICKETS:
    for i, number in enumerate(ticket):
        valid_fields = get_valid_fields(number)
        if not valid_fields:
            continue

        fields[i].append(valid_fields)

final = {k: all_fields.intersection(*v) for k, v in fields.items()}

seen = set()
while any(len(i) > 1 for i in final.values()):
    for k, v in final.items():
        value = list(v)[0]
        if len(v) == 1 and value not in seen:
            seen.add(value)
            to_remove, tag = value, k
            break

    remove_all(final, to_remove, tag)

    
formatted_ticket = {list(v)[0]: int(TICKET[k]) for k, v in final.items()}
[print(f"{k.ljust(20)} {str(v).rjust(4)}") for k, v in formatted_ticket.items()]

n = 1
for k, v in formatted_ticket.items():
    if k.startswith("departure"):
        n *= v

print(n)
