def main(x):
    bn = bin(x)[2:].rjust(25, "0")
    j4 = x & 0x1F00000
    j32 = (x & 0xFFF00) >> 8
    j0 = 0x1F00FFF
    res = (j0 & j32) | j4
    return str(res)
