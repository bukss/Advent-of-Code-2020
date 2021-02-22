from aoc_utils import load_input

#f = load_input("\n\n")

print(sum(sum(p.count(c)==p.count("\n")+1for c in p.split("\n")[0])for p in open("input.txt").read().split("\n\n")))

