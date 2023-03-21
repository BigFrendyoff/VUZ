from functools import cache


@cache
def lev_dist(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return lev_dist(a, b, i - 1, j - 1)
    else:
        return 1 + min(lev_dist(a, b, i, j - 1), lev_dist(a, b, i - 1, j), lev_dist(a, b, i - 1, j - 1))


def generate(a, b):
    return lev_dist(a, b, len(a), len(b))


print(generate('столб', 'слон'))
