import coverage

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = 10
b = 5

print("a = ", a)
print("b = ", b)

print("a + b = ", add(a, b))
print("a - b = ", subtract(a, b))
print("a * b = ", multiply(a, b))
print("a / b = ", divide(a, b))
print("a / 0 = ", divide(a, 0))

def calculate_sum(n):
    """Функция для расчета суммы чисел от 1 до n"""
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# Тестовая функция для проверки функции calculate_sum()
def test_calculate_sum():
    assert calculate_sum(3) == 6
    assert calculate_sum(5) == 15
    assert calculate_sum(-1) == 0  # Этот тест должен упасть, потому что входной параметр должен быть положительным числом

# Вызов тестовой функции
test_calculate_sum()

# как запускать
# открываем снизу терминал в самом питоне (мб надо в смд сделать pip install coverage или я вон сверху импорт сделал)
# пишем туда coverage run (путь к файлу calculator.py)
# пишем coverage report -m
# пишем coverage run --branch (путь к файлу calculator.py)
# пишем coverage report -m
# пишем coverage html
# создаст папку с файлом index.html, открываем его в браузере и радуемся