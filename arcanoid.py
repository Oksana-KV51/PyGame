#ПРОМТ: напиши простую игру арканоид с использованием языка программирования пайтон и
# библиотеки Pygame. Используй классы при написании программы

#дополни эту программу так чтобы шарик мог разрушать кирпичи

#добавь в код ниже меню при входе, которое позволит выбрать размер мяча, платвормы и скорость

import pygame
import random
import sys

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
black = (0, 0, 0)

# ФПС и таймер
clock = pygame.time.Clock()
fps = 60


# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Меню настроек
def game_menu():
    ball_size = 30
    paddle_width = 100
    movement_speed = 6

    while True:
        screen.fill(white)
        draw_text('Welcome to Breakout!', pygame.font.Font(None, 36), black, screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 100, 200, 50)
        button_2 = pygame.Rect(250, 200, 200, 50)
        button_3 = pygame.Rect(250, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                ball_size = 20
                paddle_width = 80
                movement_speed = 8
        if button_2.collidepoint((mx, my)):
            if click:
                ball_size = 30
                paddle_width = 100
                movement_speed = 6
        if button_3.collidepoint((mx, my)):
            if click:
                ball_size = 40
                paddle_width = 120
                movement_speed = 4

        pygame.draw.rect(screen, blue, button_1)
        pygame.draw.rect(screen, green, button_2)
        pygame.draw.rect(screen, red, button_3)

        draw_text('Easy', pygame.font.Font(None, 30), white, screen, 320, 110)
        draw_text('Medium', pygame.font.Font(None, 30), white, screen, 310, 210)
        draw_text('Hard', pygame.font.Font(None, 30), white, screen, 320, 310)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(fps)

        if click:
            return ball_size, paddle_width, movement_speed

# Получаем настройки из меню
ball_size, paddle_width, movement_speed = game_menu()

# Определение классов
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 75, 30)

    def draw(self):
        pygame.draw.rect(screen, green, self.rect)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, paddle_width, 20)

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
        self.rect = pygame.Rect(x, y, ball_size, ball_size)
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