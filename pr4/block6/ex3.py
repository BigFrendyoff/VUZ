OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}


def not_implemented(vm):
    raise RuntimeError('Not implemented!')

LIB = { # Для быстрого задания большинства операций полезен модуль operator
    '+': not_implemented,
    '-': not_implemented,
    '*': not_implemented,
    '/': not_implemented, # Целочисленный вариант деления
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
    '.': not_implemented,
    'emit': not_implemented,
    '?': not_implemented,
    'array': not_implemented,
    '@': not_implemented,
    '!': not_implemented
}


def disassemble(code):
    pc = 0  # счетчик команд
    stack = []  # стек
    scope = {}  # пространство имен

    while pc < len(code):
        opcode = code[pc] & 0b111  # младшие 3 бита - код операции
        operand = code[pc] >> 3  # старшие 29 бит - аргумент операции

        if opcode == 0 and operand == 0:  # entry
            print("entry:")
        elif opcode == 0:  # PUSH
            stack.append(operand)
            print("    push", operand)
        elif opcode == 1:
            if operand == 0:
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
                print("    op", "'+'")
            elif operand == 1:
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
                print("    op", "'-'")
            elif operand == 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
                print("    op", "'*'")
            elif operand == 3:
                b = stack.pop()
                a = stack.pop()
                stack.append(a // b)
                print("    op", "'/'")
            elif operand == 4:
                b = stack.pop()
                a = stack.pop()
                stack.append(a % b)
                print("    op", "'%'")
            elif operand == 5:
                b = stack.pop()
                a = stack.pop()
                stack.append(a & b)
                print("    op", "'&'")
            elif operand == 6:
                b = stack.pop()
                a = stack.pop()
                stack.append(a | b)
                print("    op", "'|'")
            elif operand == 7:
                b = stack.pop()
                a = stack.pop()
                stack.append(a ^ b)
                print("    op", "'^'")
            elif operand == 8:
                b = stack.pop()
                a = stack.pop()
                stack.append(a < b)
                print("    op", "'<'")
            elif operand == 9:
                b = stack.pop()
                a = stack.pop()
                stack.append(a > b)
                print("    op", "'>'")
            elif operand == 10:
                b = stack.pop()
                a = stack.pop()
                if (a == b):
                    stack.append(True)
                else:
                    stack.append(False)
                print("    op", "'='")
            elif operand == 11:
                b = stack.pop()
                a = stack.pop()
                stack.append(a << b)
                print("    op", "'<<'")
            elif operand == 12:
                b = stack.pop()
                a = stack.pop()
                stack.append(a >> b)
                print("    op", "'>>'")
            elif operand == 13:

                print("    op", "'if'")
            elif operand == 14:

                print("    op", "'for'")
            elif operand == 15:

                print("    op", "'.'")
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



        #elif opcode == 2:  # call

        elif opcode == 3:  # is
            value = stack.pop()
            key = stack.pop()
            scope[key] = value
            print("    is ", key)

        #elif opcode == 4:  # to


        elif opcode == 5:  # exit
            print("    exit", operand)
            break



        pc += 1  # переход к следующей команде


# Пример использования дизассемблера
code = [0, 16, 16, 1, 121, 2, 5]
disassemble(code)

def func():
    print("Hello, world!")