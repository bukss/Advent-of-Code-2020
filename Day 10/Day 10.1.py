from aoc_utils import load_input
from collections import defaultdict

adapters = [0] + list(map(int, load_input()))
adapters += [max(adapters) + 3]
adapters = list(enumerate(sorted(adapters)))

differences = defaultdict(int)

for i, n in adapters[:-1]:
    differences[adapters[i + 1][1] - n] += 1

print(differences[1] * differences[3])
