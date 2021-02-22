from aoc_utils import load_input
import re

f = load_input()

def parens(m):
    return str(left_to_right(m.group(1)))

def left_to_right(s):
    while "(" in s:
        s = re.sub(r"\((\d+( [\+\*] \d+)+)\)", parens, s)
    s = re.sub(r"((\*|\+) \d+)", r"\1)", s)
    s = "("*(s.count(")")-s.count("(")) + s
    return eval(s)

print(sum(map(left_to_right, f)))