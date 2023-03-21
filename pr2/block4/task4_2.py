import sys


def my_print(*objects, separator=' ', end="\n"):
    res = str(objects[0])
    for i in range(1, len(objects)):
        res += separator + str(objects[i])
    res += end
    sys.stdout.write(res)

