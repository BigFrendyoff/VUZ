OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}


def not_implemented(vm):
    raise RuntimeError('Not implemented!')


def implemented(vm):
    print('Implemented!')


class VirtualMachine:
    def __init__(self, code):
        self.pc = 0  # счетчик команд
        self.stack = []  # стек
        self.code = code  # память кода
        self.scope = {}  # пространство имен
        self.LIB = {  # Для быстрого задания большинства операций полезен модуль operator
            '+': self.sum_op,
            '-': not_implemented,
            '*': not_implemented,
            '/': not_implemented,  # Целочисленный вариант деления
            '%': not_implemented,
            '&': not_implemented,
            '|': not_implemented,
            '^': not_implemented,
            '<': not_implemented,
            '>': not_implemented,
            '=': not_implemented,
            '<<': not_implemented,
            '>>': not_implemented,
            'if': not_implemented,
            'for': not_implemented,
            '.': self.dot,
            'emit': not_implemented,
            '?': not_implemented,
            'array': not_implemented,
            '@': not_implemented,
            '!': not_implemented
        }

    def not_implemented(self):
        raise RuntimeError('Not implemented!')

    def sum_op(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def dot(self):
        return self.stack.pop()

    def run(self):
        while self.pc < len(self.code):
            opcode = self.code[self.pc] & 0b111  # младшие 3 бита - код операции
            operand = self.code[self.pc] >> 3  # старшие 29 бит - аргумент операции
            if opcode == 0 and operand == 0:  # entry
                print("entry:")
            elif opcode == 0:  # PUSH
                self.stack.append(operand)
                print("    push", operand)
            elif opcode == 1:
                if operand == 0:
                    self.LIB['+']()
                    print("    op", "'+'")
                elif operand == 1:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a - b)
                    print("    op", "'-'")
                elif operand == 2:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a * b)
                    print("    op", "'*'")
                elif operand == 3:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a // b)
                    print("    op", "'/'")
                elif operand == 4:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a % b)
                    print("    op", "'%'")
                elif operand == 5:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a & b)
                    print("    op", "'&'")
                elif operand == 6:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a | b)
                    print("    op", "'|'")
                elif operand == 7:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a ^ b)
                    print("    op", "'^'")
                elif operand == 8:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a < b)
                    print("    op", "'<'")
                elif operand == 9:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a > b)
                    print("    op", "'>'")
                elif operand == 10:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    if (a == b):
                        self.stack.append(True)
                    else:
                        self.stack.append(False)
                    print("    op", "'='")
                elif operand == 11:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a << b)
                    print("    op", "'<<'")
                elif operand == 12:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a >> b)
                    print("    op", "'>>'")
                elif operand == 13:

                    print("    op", "'if'")
                elif operand == 14:

                    print("    op", "'for'")
                elif operand == 15:

                    print("    op", "'.'", self.LIB['.']())
                elif operand == 16:

                    print("    op", "'emit'")
                elif operand == 17:

                    print("    op", "'?'")
                elif operand == 18:

                    print("    op", "'array'")
                elif operand == 19:

                    print("    op", "'@'")
                elif operand == 20:

                    print("    op", "'!'")



            # elif opcode == 2:  # call
            #     value = self.scope.get(operand)
            #     print(value, '----------')
            #     if callable(value):
            #         value()
            #     else:
            #         self.stack.append(value)
            #
            # elif opcode == 3:  # is
            #     self.scope[operand] = self.stack.pop()
            #     print("    is ", operand)

            # elif opcode == 4:  # to

            elif opcode == 5:  # exit
                print("    exit", operand)
                break

            self.pc += 1  # переход к следующей команде


code = [0, 16, 16, 1, 121, 5]
VM = VirtualMachine(code)
VM.run()



def func():
    print("Hello, world!")
print(func)