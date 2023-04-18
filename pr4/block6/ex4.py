import operator

class VirtualMachine:
    def __init__(self, code):
        self.pc = 0
        self.stack = []
        self.code = code
        self.scope = {}

    def run(self):
        while self.pc < len(self.code):
            instruction = self.code[self.pc]
            opcode = instruction & 0b111
            operand = instruction >> 3

            if opcode == 0b000:  # push
                self.stack.append(operand)
            elif opcode == 0b001:  # op
                fn = operator.__dict__[{
                    0: "add", 1: "sub", 2: "mul", 3: "floordiv"
                }[operand]]
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(fn(a, b))
            elif opcode == 0b010:  # call
                value = self.scope.get(operand)
                if callable(value):
                    value()
                else:
                    self.stack.append(value)
            elif opcode == 0b011:  # is
                self.scope[operand] = self.stack.pop()
            elif opcode == 0b100:  # to
                self.scope[operand] = operand
            elif opcode == 0b101:  # exit
                return
            else:
                raise ValueError(f"Unknown opcode: {opcode}")

            print(self.scope)
            self.pc += 1

code = [
    0b000_00000000000000000000000101,  # push 5
    0b000_00000000000000000000000110,  # push 6
    0b001_00000000000000000000000000,  # op add
    0b011_00000000000000000000000111,  # is func
    0b010_00000000000000000000000111,  # call func
    0b101_00000000000000000000000000,  # exit
]

def func():
    print("Hello, world!")

vm = VirtualMachine(code)
vm.scope["func"] = func
print(vm.scope["func"])
vm.run()

