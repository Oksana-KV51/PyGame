#В этом примере игровой механикой является управление игроком (белый квадрат) с помощью клавиш с
# о стрелками для избегания врагов (красные квадраты), которые двигаются в случайных направлениях.
# Игра заканчивается, как только игрок сталкивается с одним из врагов.


import pygame
import random
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ФПС
FPS = 60
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH /2, SCREEN_HEIGHT /2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # Ограничение движения по экрану
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.move_ip(self.speed, random.randint(-5, 5))
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
            self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()

all_sprites.add(player)

# Создание врагов
for _ in range(5):
    new_enemy = Enemy()
    all_sprites.add(new_enemy)
    enemies.add(new_enemy)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Обновление
    player.update()
    enemies.update()

    # Проверка коллизий
    if pygame.sprite.spritecollideany(player, enemies):
        running = False

    # Рендеринг
    screen.fill(BLACK)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()