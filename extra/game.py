import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)

pygame.init()

def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - 50
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        self.speed_y += 1
        self.rect.y += self.speed_y
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
            self.speed_y = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    p = Platform(i * 150, HEIGHT - (i * 100) - 100)
    all_sprites.add(p)
    platforms.add(p)

for i in range(10):
    c = Coin(random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20))
    all_sprites.add(c)
    coins.add(c)

score = 0
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.rect.y = hits[0].rect.y - player.rect.height
        player.speed_y = 0

    coin_hits = pygame.sprite.spritecollide(player, coins, True)
    if coin_hits:
        score += len(coin_hits)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    draw_text(screen, f"Score: {score}", 24, 10, 10, WHITE)
    pygame.display.flip()

pygame.quit()
