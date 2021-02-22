from aoc_utils import load_input

rules = load_input()

correct = 0
for rule in rules:
    tokens = rule.split(" ")
    a, b = tuple(map(int, tokens[0].split("-")))
    letter = tokens[1][0]
    password = tokens[2]
    c = password.count(letter)
    if (password[a-1] == letter) != (password[b-1] == letter):
        correct += 1

print(correct)