s = [1, 2, 2, 3, 1, 3, 4, 5, 2, 5, 2]
print(sum(list(s[i] for i in range(len(s)) if i % 2 == 0)))
