from aoc_utils import load_input
from collections import defaultdict

f = [int(i) for i in load_input(",")]
spoken = defaultdict(list)
p = 0
check = -1
n = -1

for i, n in enumerate(f):
    spoken[n].append(i)

for i in range(len(f), 30000000):

    if n in spoken.keys() and len(spoken[n]) > 1:
        n = spoken[n][0] - spoken[n][1]
    else:
        n = 0
        
    spoken[n] = [i] + spoken[n]
    if len(spoken[n]) > 2:
        del spoken[n][-1]

print(n)