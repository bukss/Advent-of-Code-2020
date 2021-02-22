from aoc_utils import load_input

f = load_input()

print(sum(len(set(p.replace("\n","")))for p in f))