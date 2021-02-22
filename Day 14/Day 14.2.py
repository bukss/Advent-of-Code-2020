import re

class Console:
    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.mem = {}
        self.mask = "X"*36

    def apply_mask(self, v):
        print(self.mask)
        b = list(str(bin(v)).replace("b", "").rjust(36, "0"))
        addresses = []
        floats = []
        for i, c in enumerate(self.mask):
            if c == "1":
                b[i] = "1"
            elif c == "X":
                floats.append(i)
        # print(2**self.mask.count("X"))
        for i in range(2**self.mask.count("X")):
            b2 = str(bin(i))[1:].replace("b","").rjust(len(floats), "0")

            for j, bit in enumerate(b2):

                b[floats[j]] = bit

            addresses.append(int("".join(b), 2))

        print(addresses)
        if not addresses:
            return [int("".join(b), 2)]
        return addresses

    def write(self, m, v):
        m = self.apply_mask(m)
        for a in m:
            self.mem[a] = v

    def run(self):
        for line in self.code:
            instruction = line.split()
            if "mask" in line:
                self.mask = instruction[-1]
            else:
                m = int(re.match(r"mem\[(.+)\]", line).groups()[0])
                v = int(instruction[-1])
                self.write(m, v)

from aoc_utils import load_input


f = load_input()
c = Console(f)
c.run()
print(sum(c.mem.values()))