from aoc_utils import load_input

numbers = [int(i) for i in load_input()]

for a in numbers:
    if (b := 2020 - a) in numbers:
        print(a * b)
        exit()
