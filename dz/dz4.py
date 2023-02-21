def main(n):
    if n == 0:
        return 0.74
    return abs(main(n - 1) ** 2 + main(n - 1) ** 3 + main(n - 1)) - 1
