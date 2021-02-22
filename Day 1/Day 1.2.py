from aoc_utils import load_input

# Golfed answer
n = [int(i) for i in load_input()]
[exit(a*b*c)for a in n for b in n if(c:=2020.-a-b)in n]
