import pygame
import random
import time

# Определение константы для задержки между кадрами
FRAME_RATE = 60

# Определение функции для задержки между кадрами
def delay():
    time.sleep(1 / FRAME_RATE)

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")

# Определение констант
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Определение класса змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * BLOCK_SIZE)), (cur[1] + (y * BLOCK_SIZE)))
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Определение констант для направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Определение класса еды
class Food:
    def __init__(self):
        x = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)
        self.position = (x, y)
        self.color = RED

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Определение функции для обновления экрана
def update_screen():
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.update()

# Создание объектов
snake = Snake()
food = Food()

# Основной игровой цикл
while True:
    snake.handle_keys()
    snake.move()
    if snake.get_head_position() == food.position:
        snake.length += 1
        food = Food()
    update_screen()
    pygame.time.Clock().tick(SNAKE_SPEED)


