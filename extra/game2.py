import time

import pygame
import random
import auth
# инициализация Pygame
pygame.init()

# настройки окна
window_width = 800
window_height = 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("2D Field")

# настройки графического объекта
object_width = 50
object_height = 50
object_color = (255, 0, 0)  # красный цвет
object_x = window_width // 2 - object_width // 2  # начальная позиция объекта по горизонтали
object_y = window_height // 2 - object_height // 2  # начальная позиция объекта по вертикали
object_speed = 0.2  # скорость перемещения объекта
object_gravity = 0.1  # сила тяжести объекта

# настройки геометрических объектов
geometry_count = 10  # количество геометрических объектов
geometry_width = 50
geometry_height = 50
geometry_color = (0, 255, 0)  # зеленый цвет
geometries = []  # список геометрических объектов
for i in range(geometry_count):
    x = random.randint(0, window_width - geometry_width)
    y = random.randint(0, window_height - geometry_height)
    geometries.append(pygame.Rect(x, y, geometry_width, geometry_height))

# настройки счетчика
score = 0
score_font = pygame.font.SysFont("Arial", 30)

# основной цикл игры
running = False

users = {}

def register(username, password):
    if username not in users:
        users[username] = password
        print("Registration successful!")
    else:
        print("Username already exists!")

def login(username, password):
    if username in users:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")


username = input('Enter username: ')
password = input('Enter password: ')
if username not in users:
    users.setdefault(username, password)
    print("Registration successful!")
if username in users:
    if users[username] == password:
        print("Login successful!")
        time.sleep(3)
        running = True
    else:
        print("Incorrect password!")


while running:
    # проверка выхода объекта за границы окна
    if object_x < 0:
        object_x = 0
        running = False
    elif object_x + object_width > window_width:
        object_x = window_width - object_width
        running = False
    if object_y < 0:
        object_y = 0

        running = False
    elif object_y + object_height > window_height:
        object_y = window_height - object_height
        running = False

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # проверка нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_x -= object_speed
    if keys[pygame.K_RIGHT]:
        object_x += object_speed
    if keys[pygame.K_UP]:
        object_y -= object_speed
    if keys[pygame.K_DOWN]:
        object_y += object_speed

    # применение силы тяжести к объекту
    object_y += object_gravity

    # проверка коллизий объекта с геометрическими объектами
    for geometry in geometries:
        if pygame.Rect(object_x, object_y, object_width, object_height).colliderect(geometry):
            score += 1
            geometries.remove(geometry)
            x = random.randint(0, window_width - geometry_width)
            y = random.randint(0, window_height - geometry_height)
            geometries.append(pygame.Rect(x, y, geometry_width, geometry_height))

    # отображение графических объектов на экране
    window.fill((255, 255, 255))  # белый фон
    pygame.draw.rect(window, object_color, (object_x, object_y, object_width, object_height))  # графический объект
    for geometry in geometries:
        pygame.draw.rect(window, geometry_color, geometry)  # геометрические объекты

    # отображение счетчика на экране
    score_text = score_font.render("Score: {}".format(score), True, (0, 0, 0))  # черный цвет текста
    window.blit(score_text, (10, 10))  # отображение текста в левом верхнем углу

    # обновление экрана
    pygame.display.update()

# завершение работы Pygame
pygame.quit()