from aoc_utils import load_input

rules = load_input()

correct = 0
for rule in rules:
    tokens = rule.split(" ")
    min_count, max_count = tuple(map(int, tokens[0].split("-")))
    letter = tokens[1][0]
    password = tokens[2]
    c = password.count(letter)
    if min_count <= c <= max_count:
        correct += 1

print(correct)

