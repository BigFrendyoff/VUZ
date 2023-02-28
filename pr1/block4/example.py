import math


def main(x, y, z):
    return ((z ** 3 + x + y ** 2 - 74 * (65 * z + y ** 2) ** 7) / (
            (85 - 76 * y ** 2 - x ** 3) ** 5 + math.log(80 * y ** 2 - 72 * z - y ** 3) ** 4)) + 43 * (
                       42 + 59 * y) ** 2 - 54 * (5 * x - z ** 3) ** 4

print(main(-0.36, -0.4, 0.45))
print(main(0.63, 0.42, -0.75))
print(main(-0.14, -0.94, -0.36))
print(main(-0.61, -0.82, -0.24))