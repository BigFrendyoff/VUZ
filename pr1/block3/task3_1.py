def multiply_by_twelve(x):
    x += x
    x += x
    temp = x
    x += x
    x += temp
    return x

print(multiply_by_twelve(3))