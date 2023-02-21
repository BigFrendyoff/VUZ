def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16k(x, y):
    xfirst = (x & 0xFF00) >> 8
    xlast = x & 0x00FF
    yfirst = (y & 0xFF00) >> 8
    ylast = y & 0x00FF

    xf_yf = mul_bits(xfirst, yfirst, 8)
    xl_yl = mul_bits(xlast, ylast, 8)
    x_sum = xfirst + xlast
    y_sum = yfirst + ylast
    xs_ys = mul_bits(x_sum, y_sum, 8)
    substraction = xs_ys - xf_yf - xl_yl
    return (xf_yf << 16) + (substraction << 8) + xl_yl

print(mul_16k(781, 698))
