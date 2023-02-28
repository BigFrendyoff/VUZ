s = ['much', 'code2', 'wow']
print(list(q for q in s if len(q) == (max(list(len(i) for i in s))))[0])