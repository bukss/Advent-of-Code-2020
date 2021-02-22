from aoc_utils import load_input
import re

f = load_input("\n\n")

def rewrite(m):
    c = rules[m.group(1)]
    return f"({c})"


def expand_rule(r):
    rule = rules[r]
    while any(c.isdigit() for c in rule):
        rule = re.sub(r"(\d+)", rewrite, rule)

    rule = rule.replace(" ", "").replace("\"", "")
    return rule


possible_11_patterns = []
for i in range(4, 0, -1):
    possible_11_patterns.append(f"({'42 '*i} {'31 '*i})")

f[0] = f[0].replace("8: 42", "8: (42)+")
f[0] = f[0].replace("11: 42 31", "11: " + "|".join(possible_11_patterns))

rule_info, msgs = [i.splitlines() for i in f]
rules = {}

for rule in rule_info:
    num, r = re.match(r"(\d+): (.*)$", rule).group(1, 2)
    rules[num] = r


pattern = expand_rule("0")
counter = sum([bool(re.fullmatch(pattern, msg)) for msg in msgs])
print(counter)
