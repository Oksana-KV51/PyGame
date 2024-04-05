#игра пинг-понг

import pygame
import random

pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_RADIUS = 7
WHITE = (255, 255, 255)
FPS = 60

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пинг-Понг")

clock = pygame.time.Clock()

# Классы, описывающие игроков и мяч
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.score = 0

    def move(self, y):
        self.rect.y += y
        self.rect.y = max(self.rect.y, 0)
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - PADDLE_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])

# Инициализация игрока, компьютера и мяча
player = Paddle(SCREEN_WIDTH - PADDLE_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
computer = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(-10)
    if keys[pygame.K_DOWN]:
        player.move(10)

    if ball.dx < 0:
        if computer.rect.centery < ball.rect.centery:
            computer.move(7)
        else:
            computer.move(-7)

    ball.move()

    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(computer.rect):
        ball.dx = -ball.dx

    if ball.rect.left <= 0:
        player.score += 1
        ball.reset()

    if ball.rect.right >= SCREEN_WIDTH:
        computer.score += 1
        ball.reset()

    screen.fill((0, 0, 0))
    player.draw()
    computer.draw()
    ball.draw()

    if player.score == 10 or computer.score == 10:
        running = False

    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры и вывод результатов
print(f"Игрок пропустил: {computer.score} мячей")
print(f"Компьютер пропустил: {player.score} мячей")
pygame.quit()