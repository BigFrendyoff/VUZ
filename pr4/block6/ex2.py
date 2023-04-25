import operator

OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}



def not_implemented():
    raise RuntimeError('Not implemented!')


def implemented():
    print('Implemented!')


LIB = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '%': operator.mod,
    '&': operator.and_,
    '|': operator.or_,
    '^': operator.xor,
    '<': operator.lt,
    '>': operator.gt,
    '=': operator.eq,
    '<<': operator.lshift,
    '>>': operator.rshift,
    'if': not_implemented,
    'for': not_implemented,
    '.': lambda x: print(x, end=''),
    'emit': lambda x: print(chr(x), end=''),
    '?': not_implemented,
    'array': not_implemented,
    '@': not_implemented,
    '!': not_implemented
}

LIB_KEYS = list(LIB.keys())

class VirtualMachine:
    def __init__(self, code):
        self.entry = code[0]  # счетчик команд
        self.stack = []  # стек
        self.code = code[1:]  # память кода
        self.scope = {}  # пространство имен

    def run(self, scope=dict()):
        scope = scope.copy()
        pc = self.entry
        while pc < len(self.code):
            opcode = self.code[pc] & 0b111
            operand = self.code[pc] >> 3
            op = OP_NAMES[opcode]

            if op == 'push':  # PUSH
                self.stack.append(operand)
            if op == 'op':

                if 0 <= operand <= 12:
                    self.stack.append(LIB[LIB_KEYS[operand]](self.stack.pop(), self.stack.pop()))
                else:
                    self.stack.append(LIB[LIB_KEYS[operand]](self.stack.pop()))

            if op == 'is':
                scope[operand] = (self.stack.pop(), 'f')

            if op == 'call':
                if scope[operand][1] == "f":
                    self.entry = scope[operand][0]
                    self.run(scope)
                if scope[operand][1] == 'v':
                    self.stack.append(scope[operand][0])

            if op == 'exit':
                break

            pc += 1


code = [57, 8440, 129, 8704, 129, 8688, 129, 8600, 129, 8704, 129, 8576, 129, 8672,
 129, 8672, 129, 8576, 129, 256, 129, 8728, 129, 8712, 129, 8696, 129, 8616,
 129, 8768, 129, 8680, 129, 8688, 129, 256, 129, 8592, 129, 8792, 129, 8696,
 129, 8688, 129, 8664, 129, 8680, 129, 8616, 129, 8680, 129, 8576, 129, 264,
 129, 5, 0, 3, 2, 5]

VM = VirtualMachine(code)
VM.run()
