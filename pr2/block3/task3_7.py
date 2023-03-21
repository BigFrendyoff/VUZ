x = 100

print("Число харшад" if x % sum(list(int(i) for i in list(str(x)))) == 0 else "Не число харшад" )