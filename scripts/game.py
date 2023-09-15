import pygame
import pickle
import os
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

TILE_SIZE = 40

# load bg
sky = pygame.image.load('assets\images\sky.png').convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
sun = pygame.image.load('assets\images\sun.png').convert_alpha()
sun = pygame.transform.scale(sun, (TILE_SIZE * 1.5, TILE_SIZE * 1.5))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky, (0, 0))
    screen.blit(sun, (100, 50))

    pygame.display.update()
    clock.tick(FPS)