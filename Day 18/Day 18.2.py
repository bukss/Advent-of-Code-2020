from aoc_utils import load_input
import re

f = load_input()

def parens(m):
    return str(calc(m.group(1)))

def reval(m):
    return str(eval(m.group(1)))

def calc(s):
    while "(" in s:
        s = re.sub(r"\((\d+( [\+\*] \d+)+)\)", parens, s)
    s = re.sub(r"(\d+( \+ \d+)+)", reval, s)
    return eval(s)

print(sum(map(calc, f)))