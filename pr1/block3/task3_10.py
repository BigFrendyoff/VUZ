import math


def fast_mul_gen(y):
    print('def mul(x, y):')
    print(' t = x')
    print(' if y == 0:\n'
          '     return 0')
    for i in range(y - 1):
        print(' x += t')
    print(' return x')

math.log()

def fast_pow_gen(y):
    fast_mul_gen(y)
    print()
    print('def pow(x, y):')
    print(' res = x')
    print(' if y == 0:')
    print('     return 1')
    for i in range(y - 1):
        print(' res = mul(res, x)')
    print(' return res')

fast_pow_gen(1)