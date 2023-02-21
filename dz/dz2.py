import math


def main(x):
    if (x < 130):
        return x ** 2
    if (130 <= x < 228):
        return 81 * x ** 21
    if (x >= 228):
        return x ** 5 + 15 * (56 * x) ** 4 + 98 * math.log10(x) ** 2
