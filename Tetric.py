# тетрис

import pygame
import random

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Размеры экрана и блоков
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BLOCK_SIZE = 20

# Настройки игры
game_difficulties = {'Легко': 0.5, 'Средне': 0.3, 'Сложно': 0.1}


class Tetris:
    def __init__(self, column_count, row_count):
        self.columns = column_count
        self.rows = row_count
        self.board = [[0] * column_count for _ in range(row_count)]
        self.score = 0
        self.game_over = False

    def add_piece(self):
        # Это место для добавления новой фигурки
        pass

    def check_lines(self):
        # Это место для проверки и удаления заполненных линий
        pass

    def update(self):
        # Обновление состояния игры, вызов check_lines, перемещение фигуры
        if self.game_over:
            return
        self.score += 1

    def draw(self, screen):
        # Отрисовка доски и текущего состояния игры
        for y in range(self.rows):
            for x in range(self.columns):
                if self.board[y][x]:
                    pygame.draw.rect(screen, WHITE, [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])


## Добавляем функции отображения меню и завершения игры
def main_menu(screen):
    run = True
    selected_difficulty = 'Средне'
    while run:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    selected_difficulty = 'Сложно' if selected_difficulty == 'Средне' else 'Средне'
        # Здесь будет код отрисовки меню

        pygame.display.flip()
    return game_difficulties[selected_difficulty]


def game_over_screen(screen, score):
    run = True
    while run:
        screen.fill(BLACK)
        # Отрисовка сообщения о завершении игры и счета

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
        pygame.display.flip()


# Инициализация и главный игровой цикл
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Тетрис')

game_speed = main_menu(screen)
tetris = Tetris(SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)

clock = pygame.time.Clock()
while not tetris.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tetris.game_over = True

    tetris.update()
    screen.fill(BLACK)
    tetris.draw(screen)
    pygame.display.flip()
    clock.tick(game_speed * 60)

game_over_screen(screen, tetris.score)
pygame.quit()