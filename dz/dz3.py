def main(a, b, m, x):
    sum = 0
    for k in range(1, m + 1):
        for i in range(1, b + 1):
            for c in range(1, a + 1):
                sum += (pow(73 * k ** 2 + c ** 3, 6)
                        - 10 * pow(i ** 2 + x / 64, 5))
    return sum
