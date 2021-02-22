from aoc_utils import load_input

import re

class Console:
    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.mem = {}
        self.mask = "X"*36

    def apply_mask(self, v):
        b = list(str(bin(v).replace("b", "")).rjust(36, "0"))
        for i, c in enumerate(self.mask):
            if c in "01":
                b[i] = c
        return int("".join(b), 2)

    def write(self, m, v):
        v = self.apply_mask(v)
        self.mem[m] = v

    def run(self):
        for line in self.code:
            instruction = line.split()
            if "mask" in line:
                self.mask = instruction[-1]
            else:
                m = int(re.match(r"mem\[(.+)\]", line).groups()[0])
                v = int(instruction[-1])
                self.write(m, v)

f = load_input()
c = Console(f)
c.run()
print(sum(c.mem.values()))
