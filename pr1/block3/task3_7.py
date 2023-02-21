def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16(x, y):
    xfirst = (x & 0xFF00) >> 8
    xlast = x & 0x00FF
    yfirst = (y & 0xFF00) >> 8
    ylast = y & 0x00FF

    return mul_bits(xlast, ylast, 8) + ((mul_bits(xlast, yfirst, 8)
                                         + mul_bits(xfirst, ylast, 8)) << 8) + (
                   mul_bits(xfirst, yfirst, 8) << 16)


print(mul_16(781, 450))
