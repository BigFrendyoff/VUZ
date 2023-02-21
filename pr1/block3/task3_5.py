import random


def fast_mul(x, y):
    sum = 0
    if (x == 0 or y == 0):
        return 0
    if (x % 2 != 0):
        sum += y
    if (x == 1):
        return sum
    while(True):
        x //= 2
        y *= 2
        if (x % 2 != 0):
            sum += y
        if (x == 1):
            return sum

for i in range(1000):
    x = int(random.random() * 100)
    y = int(random.random() * 100)
    res = fast_mul(x, y)
    # print(f'{x} * {y} = {res}')
    assert x * y == res, f"Ошибка: x({x}) * y({y}) = {x * y}, а в функции: {res}"
