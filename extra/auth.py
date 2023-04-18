import hashlib

# Словарь, где будут храниться пользователи
users = {}

# Функция регистрации пользователя
def register(username, password):
    # Хешируем пароль
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Добавляем пользователя в словарь
    users[username] = hashed_password
    print("Вы успешно зарегистрировались!")

# Функция входа
def login(username, password):
    # Проверяем, есть ли такой пользователь в словаре
    if username in users:
        # Хешируем введенный пароль
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Сравниваем хешированные пароли
        if users[username] == hashed_password:
            return True
        else:
            return False
    else:
        print("Такой пользователь не зарегистрирован!")


