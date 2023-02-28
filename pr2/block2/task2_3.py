a = 1
b = 1
c = 300000
d = 300000
print(a is b, c is d)
print(id(a), id(b), id(c), id(d))

a, b = 'py', 'py'
c = ''.join(['p', 'y'])
print(a is b, a == c, a is c)
print(id(a), id(b), id(c))