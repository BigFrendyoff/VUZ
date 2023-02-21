import math


def main(z, y, x):
    sum = 0
    for i in range(1, len(z) + 1):
        sum += ((math.sqrt(x[i - 1] ** 3
                           + y[i - 1] ** 2
                           + 54 * z[math.ceil(i / 4) - 1])) ** 3) / 81
    return sum
