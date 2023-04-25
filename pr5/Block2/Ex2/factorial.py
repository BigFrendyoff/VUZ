def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def get_input():
    while True:
        try:
            n = int(input("Введите число для вычисления факториала: "))
            if n < 0:
                raise ValueError
            else:
                return n
        except:
            raise ValueError

# if __name__ == "__main__":
#     num = get_input()
#     result = factorial(num)
#     print(f"{num}! = {result}")