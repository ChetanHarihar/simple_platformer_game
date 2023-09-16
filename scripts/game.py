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

class Player:
    def __init__(self):
        self.img = pygame.image.load('assets\images\guy1.png')
        self.img = pygame.transform.scale(self.img, (TILE_SIZE, TILE_SIZE * 2))
        self.rect = self.img.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.jumped = False
        self.gravity = 0

    def update(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_LEFT]:
            dx -= 5

        self.rect.x += dx

        screen.blit(self.img, self.rect)

player = Player()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky, (0, 0))
    screen.blit(sun, (100, 50))

    player.update()

    pygame.display.update()
    clock.tick(FPS)