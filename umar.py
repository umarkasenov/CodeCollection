import pygame
import random
import time
FRAME_RATE = 60

def delay():
    time.sleep(1 / FRAME_RATE)

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Моя Игра")

class You:
    def __init__(self):
        self.length = 1
        self.positions = [(width / 2, height / 2)]
        self.direction = random.choices([UP, DOWN, LEFT, RIGHT])
        self.color = BLACK
    # Здесь вы можете добавить код для отрисовки и обновления игры
    def get_head_position(self):
        return self.positions[0]
