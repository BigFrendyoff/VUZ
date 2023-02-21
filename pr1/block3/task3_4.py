import random


def naive_mul(x, y):
    if y == 0: return 0
    r = x
    for i in range(0, y - 1):
        x += r
    return x


for i in range(1000):
    x = int(random.random() * 100)
    y = int(random.random() * 100)
    assert x * y == naive_mul(x, y), f"Ошибка: x({x}) * y({y}) = {x * y}, а в функции: {naive_mul(x, y)}"

# Неправильное выделение
# Ненужный end
# Ненужные точки с запятыми
# Нет возвращаемого значения в функции
# Складывать не с 1, а с самим собой
# Ввести условие для умножения на 0
