def decode_val(message):
    val = str(bin(message))[2:].rjust(24, "0")
    operational = []
    q = 0
    res = '0b'
    for i in range(8):
        resstr = ''
        for j in range(3):
            resstr += val[q]
            q += 1
        operational.append(resstr)
    for i in operational:
        x = i.count('0')
        if x == 3 or x == 2:
            res += "0"
        else:
            res += '1'
    return int(res, 2)


tsk = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
       6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
       2067967, 2068456]

for i in tsk:
    print(decode_val(i), end=" ")