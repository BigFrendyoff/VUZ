import random

mx = 12
print(''.join(list(chr(int(random.randint(65, 128))) for i in range(random.randint(1, mx + 1)))))