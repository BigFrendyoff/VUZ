def generate_groups():
    res = []
    for i in range(1, 9):
        res.append(f'ИВБО-{str(i).rjust(2, "0")}-21')
    for i in range(1, 34):
        res.append(f'ИКБО-{str(i).rjust(2, "0")}-21')
    for i in range(1, 3):
        res.append(f'ИМБО-{str(i).rjust(2, "0")}-21')
    for i in range(1, 14):
        res.append(f'ИНБО-{str(i).rjust(2, "0")}-21')
    return res


print(generate_groups())