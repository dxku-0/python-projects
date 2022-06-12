import sys
import random
import pygame
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, 14)
        self.y = random.randint(0, 14)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 140), fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * cell_size), int(block.y_ * cell_size, cell_size, cell_size))


pygame.init()

cell_size = 40
cell_number = 15
# screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # pygame.quit() is not enough bc some parts of the program might still be running, so we use sys.exit() too
            sys.exit()

    screen.fill((175, 215, 70))
    fruit.draw()
    pygame.display.update()
    clock.tick(60)  
