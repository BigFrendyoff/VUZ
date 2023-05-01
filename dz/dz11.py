import struct

TYPES = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    double='d',
    float='f',
)


def unpack(data, offset, type):
    return struct.unpack_from(f'<{TYPES[type]}',
                              data, offset)[0],\
           offset + struct.calcsize(TYPES[type])


def unpack_a(data, offset):
    result = {}
    a1, offset = unpack(data, offset, "int64")
    a2, offset = unpack(data, offset, "uint64")
    a3, offset = unpack_b(data, offset)
    new_offset, offset = unpack(data, offset, 'uint32')
    a4 = unpack_c(data, new_offset)
    a5, offset = unpack_d(data, offset)
    a6, offset = unpack_g(data, offset)
    a7, offset = unpack_h(data, offset)
    result['A1'] = a1
    result['A2'] = a2
    result['A3'] = a3
    result['A4'] = a4
    result['A5'] = a5
    result['A6'] = a6
    result['A7'] = a7

    return result


def unpack_b(data, offset):
    result = {}
    b1, offset = unpack(data, offset, 'int64')
    b2, offset = unpack(data, offset, 'int64')
    b3, offset = unpack(data, offset, 'int8')
    result['B1'] = b1
    result['B2'] = b2
    result['B3'] = b3
    return result, offset


def unpack_c(data, offset):
    result = {}
    c1 = ''
    for i in range(3):
        temp, offset = unpack(data, offset, 'char')
        c1 += str(temp)[2:-1]
    c2, offset = unpack(data, offset, 'int64')
    result['C1'] = c1
    result['C2'] = c2
    return result


def unpack_d(data, offset):
    result = {}
    size, offset = unpack(data, offset, "uint16")
    d1 = []
    e_offset, offset = unpack(data, offset, 'uint32')
    for i in range(size):
        temp, e_offset = unpack_e(data, e_offset)
        d1.append(temp)
    d2, offset = unpack(data, offset, 'uint32')
    d3, offset = unpack(data, offset, 'int64')
    f_offset, offset = unpack(data, offset, 'uint16')
    d4 = unpack_f(data, f_offset)
    d5, offset = unpack(data, offset, 'int32')
    d6, offset = unpack(data, offset, 'int8')
    result['D1'] = d1
    result['D2'] = d2
    result['D3'] = d3
    result['D4'] = d4
    result['D5'] = d5
    result['D6'] = d6
    return result, offset


def unpack_e(data, offset):
    result = {}
    e1, offset = unpack(data, offset, 'int64')
    e2, offset = unpack(data, offset, 'float')
    e3, offset = unpack(data, offset, 'uint16')
    e4, offset = unpack(data, offset, 'int8')
    e5, offset = unpack(data, offset, 'int8')
    e6 = []
    for i in range(8):
        temp, offset = unpack(data, offset, 'int8')
        e6.append(temp)
    result['E1'] = e1
    result['E2'] = e2
    result['E3'] = e3
    result['E4'] = e4
    result['E5'] = e5
    result['E6'] = e6
    return result, offset


def unpack_f(data, offset):
    result = {}
    f1, offset = unpack(data, offset, 'uint32')
    f2, offset = unpack(data, offset, 'uint32')
    f3, offset = unpack(data, offset, 'int64')
    size, offset = unpack(data, offset, 'uint32')
    arr_offset, offset = unpack(data, offset, 'uint16')
    f4 = []
    for i in range(size):
        temp, arr_offset = unpack(data, arr_offset, 'uint8')
        f4.append(temp)
    result['F1'] = f1
    result['F2'] = f2
    result['F3'] = f3
    result['F4'] = f4
    return result


def unpack_g(data, offset):
    result = {}
    g1, offset = unpack(data, offset, 'uint8')
    g2, offset = unpack(data, offset, 'int16')
    result['G1'] = g1
    result['G2'] = g2
    return result, offset


def unpack_h(data, offset):
    result = {}
    size, offset = unpack(data, offset, 'uint16')
    arr_offset, offset = unpack(data, offset, 'uint16')
    h1 = []
    for i in range(size):
        temp, arr_offset = unpack(data, arr_offset, 'int64')
        h1.append(temp)
    h2, offset = unpack(data, offset, 'uint32')
    result['H1'] = h1
    result['H2'] = h2
    return result, offset


def main(data):
    return unpack_a(data, 3)
