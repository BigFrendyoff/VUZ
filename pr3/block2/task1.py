from matplotlib import pyplot as plt
from matplotlib import colors as cl
import random

a = 100
b = 100
data = [[0 for i in range(a)] for q in range(b)]
for x in range(0, a, 10):
    for y in range(0, b, 10):
        for i in range(8):
            for j in range(8):
                p = random.randint(0, 9)
                data[i + x][j + y] = p
                data[i + x][y + 7 - j] = p


plt.imshow(data, cmap=cl.ListedColormap())
plt.show()

