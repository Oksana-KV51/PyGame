#ПРОМТ: напиши простую игру арканоид с использованием языка программирования пайтон и
# библиотеки Pygame. Используй классы при написании программы

#дополни эту программу так чтобы шарик мог разрушать кирпичи

#

import pygame
import random

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# ФПС и таймер
clock = pygame.time.Clock()
fps = 60

# Определение классов
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 75, 30)

    def draw(self):
        pygame.draw.rect(screen, green, self.rect)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 20)

    def draw(self):
        pygame.draw.rect(screen, blue, self.rect)

    def move(self, movement):
        self.rect.x += movement
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - 100:
            self.rect.x = screen_width - 100


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])

    def draw(self):
        pygame.draw.ellipse(screen, red, self.rect)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x <= 0 or self.rect.x >= screen_width - 10:
            self.dx = -self.dx
        if self.rect.y <= 0:
            self.dy = -self.dy

        # Обработка столкновения с ракеткой
        if self.rect.colliderect(paddle.rect):
            self.dy = -self.dy

         # Обработка столкновения с кирпичами
        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                self.dy = -self.dy
                bricks.remove(brick)
                break

        # Проверка пропуска шарика
        if self.rect.y > screen_height:
            self.__init__(300, 400)  # Сброс в центр


# Конфигурации для кирпичей
bricks = []
brick_width = 75
brick_height = 30
rows = 5
cols = screen_width // brick_width
for row in range(rows):
    for col in range(cols):
        brick = Brick(col * brick_width, row * brick_height)
        bricks.append(brick)


# Создание объектов
paddle = Paddle(screen_width // 2, screen_height - 30)
ball = Ball(300, 400)

# Управление движением
movement_speed = 6
movement = 0

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = -movement_speed
            if event.key == pygame.K_RIGHT:
                movement = movement_speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                movement = 0

    paddle.move(movement)
    ball.move()

    screen.fill(white)
    paddle.draw()
    ball.draw()

    # Рисуем кирпичи
    for brick in bricks:
        brick.draw()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()