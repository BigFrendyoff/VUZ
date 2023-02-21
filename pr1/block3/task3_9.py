def fast_mul_gen(y):
    print('def mul(x, y):')
    print(' t = x')
    print(' if y == 0:\n'
          '     return 0')
    for i in range(y - 1):
        print(' x += t')
    print(' return x')

fast_mul_gen(4)