from aoc_utils import load_input
import re

f = load_input("\n\n")


def hgt(x):
    if "cm" in x:
        return 150 <= int(re.findall(r"hgt\:(\d*)cm", x)[0]) <= 193
    if "in" in x:
        return 59 <= int(re.findall(r"hgt\:(\d*)in", x)[0]) <= 76

tags = {
# tag is a number in a certain range
"byr:": lambda x: 1920      <= int(re.findall(r"byr\:(\d*)", x)[0]) <= 2002,
"iyr:": lambda x: 2010      <= int(re.findall(r"iyr\:(\d*)", x)[0]) <= 2020,
"eyr:": lambda x: 2020      <= int(re.findall(r"eyr\:(\d*)", x)[0]) <= 2030,
"pid:": lambda x: 100000000 <= int(re.findall(r"eyr\:(\d*)", x)[0]) <= 999999999,

 # tag is a hex code
"hcl:": lambda x: bool(re.findall(r"hcl\:#([a-f0-9]{6})", x)),

 # tag is in a given set
"ecl:": lambda x:  any(("ecl:" + i) in x for i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),

 # tag is in a given set
"hgt:": hgt
}

c = 0
for pp in f:
    if not all(i in pp for i in tags.keys()):
        continue

    correct = all((validate(pp) for validate in tags.values()))
    if correct:
        c += 1

print(c)
