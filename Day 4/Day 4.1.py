from aoc_utils import load_input

f = load_input("\n\n")

c = 0
for pp in f:
    tags = ["ecl:", "byr:", "iyr:", "hgt:", "hcl:", "eyr:", "pid:"]
    if all(i in pp for i in tags):
        c += 1

print(c)