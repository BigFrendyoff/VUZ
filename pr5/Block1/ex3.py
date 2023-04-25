#Менеджером контекста называется объект, реализующий вышеобозначенные методы __enter__() и __exit__().
class my_raises1:
    #Сохраняет переданную в себя ошибку
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        return self
    #Начинаем проверку ошибки
    def __exit__(self, exc_type, exc_val, exc_tb):
        #проверяем наличие ошибки
        if exc_type is None:
            raise AssertionError(f"{self.expected_exception} ошибка не была вызвана")
        #проверяем совпадение типов ошибки
        if not issubclass(exc_type, self.expected_exception):
            raise AssertionError(f"{self.expected_exception} ошибка не сошлась")
            return False
        #если ошибки были вызвано верно, то напишем, что ошибки сошлись
        print("Ошибки сошлись")
        return True

#Функция создает ошибку
def myfunc():
    raise ValueError("Ошибка")

#В класс передаем нужную нам ошибку
with my_raises1(ValueError) as e:
    myfunc()