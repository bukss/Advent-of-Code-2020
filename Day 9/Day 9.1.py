from aoc_utils import load_input

f = list(map(int, load_input()))

def find(n, seq):
    for i in seq:
        if n - i in seq:
            return True

    return None

for i, n in enumerate(f[5:]):
    seq = f[i:i+25]
    test = f[i+25]
    if not find(test, seq):
        print(test)
        break