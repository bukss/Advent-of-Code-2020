from aoc_utils import load_input
from itertools import count

f = load_input()
card, door = int(f[0]), int(f[1])

def transform(val, sub=7):
    return (val*sub) % 20201227

def find_loop(public):
    val = 1
    for i in count(1):
        val = transform(val)
        if val == public:
            return i

card_loop = find_loop(card)
key = 1
for i in range(card_loop):
    key = transform(key, door)

print(key)
