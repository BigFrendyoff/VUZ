import pygame

import random



# Инициализация Pygame

pygame.init()



# Создание экрана

screen_width = 800

screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Avoid the Obstacles")



# Загрузка изображения игрока и препятствий

player_image = pygame.image.load('player.png')

obstacle_image = pygame.image.load('obstacle.png')



# Задание начальных координат игрока и препятствий

player_x = 350

player_y = 500

obstacle_x = random.randint(0, screen_width - 50)

obstacle_y = -50



# Задание скорости игрока и препятствий

player_speed = 5

obstacle_speed = 3



# Функция для создания нового препятствия

def create_obstacle():

    global obstacle_x, obstacle_y

    obstacle_x = random.randint(0, screen_width - 50)

    obstacle_y = -50



# Основной цикл игры

running = True

while running:

    # Обработка событий Pygame

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    # Движение игрока по экрану

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:

        player_x -= player_speed

    elif keys[pygame.K_RIGHT] and player_x < screen_width - 50:

        player_x += player_speed



    # Движение препятствия по экрану

    obstacle_y += obstacle_speed

    if obstacle_y > screen_height:

        create_obstacle()



    # Проверка на столкновение игрока с препятствием

    if player_x < obstacle_x + 50 and player_x + 50 > obstacle_x and player_y < obstacle_y + 50 and player_y + 50 > obstacle_y:

        create_obstacle()



    # Отображение изображений на экране

    screen.fill((255, 255, 255))

    screen.blit(player_image, (player_x, player_y))

    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    pygame.display.update()



# Завершение Pygame

pygame.quit()