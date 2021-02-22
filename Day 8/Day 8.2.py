from aoc_utils import load_input
from Computer import Console

f = load_input()

indices = [(i, o) for i, o in enumerate(f) if "jmp" in o or "nop" in o]

for i, instruction in indices:
    code = f.copy()
    if "jmp" in instruction:
        code[i] = instruction.replace("jmp", "nop")
    else:
        code[i] = instruction.replace("nop", "jmp")

    c = Console(code)
    if c.run():
        print(c.acc)
        break

