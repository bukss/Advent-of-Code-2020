class Console:
    def __init__(self, code):
        self.code = code
        self.acc = 0
        self.pointer = 0
        self.instructions = set()
        self.instruction_counter = 0
    
    def debug(self):
        self.instruction_counter += 1
        i = self.code[self.pointer].split()
        op, arg = i[0], int(i[1])

        print(f"======== [{self.instruction_counter}] ========")
        print(f"Pointer: {self.pointer}")
        print(f"Accumulator: {self.acc}")
        print(f"Instruction: {op}")
        print(f"Argument: {arg}")

        if "acc" in op:
            print(f"Accumulator increment by {arg}: {self.acc} => {self.acc + arg}")
        elif "jmp" in op:
            print(f"Pointer jump by {arg}: {self.pointer} => {self.pointer + arg}")
        elif "nop" in op:
            print("No operation")
        
        print()

    def run(self, debug = False):
        while 1:
            # Return True if halting succesfully, return False if repeating an instruction
            if self.pointer >= len(self.code):
                return True
            if self.pointer in self.instructions:
                return False
            self.instructions.add(self.pointer)

            if debug:
                self.debug()

            # Parse out the operation and argument
            i = self.code[self.pointer].split()
            op, arg = i[0], int(i[1]) 
            if "acc" in op:
                self.acc += arg
            elif "jmp" in op:
                self.pointer += arg
                continue

            self.pointer += 1