def multiply_by_fifteen(x):
    temp = x
    x += x
    x += x
    x += x
    temp = temp - x
    x = x - temp
    return x

print(multiply_by_fifteen(2))