def main(table):
    table = [list(dict.fromkeys(table[i])) for i in range(len(table))]
    unique = []
    [unique.append(i) for i in table if i not in unique]
    table = unique
    result = [[] for i in range(4)]
    for row in range(len(table)):
        result[0].append(f'{table[row][0].split(".")[0]}.'
                         f'{table[row][0].split(".")[2]}')
        result[1].append(f'{round(float(table[row][1]) * 100)}%')
        result[2].append(table[row][2].split("]")[1])
        result[3].append("-".join(table[row][3].split(".")[-1::-1]))

    return result
