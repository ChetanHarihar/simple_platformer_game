import pygame
from sys import exit
import pickle
from button import Button
import os

pygame.init()

# dimensions

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SIDE_MARGIN = 200
BOTTOM_MARGIN = 100

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + BOTTOM_MARGIN))
pygame.display.set_caption('Level Editor')

clock = pygame.time.Clock()
FPS = 60

# variables

build = True

TILE_SIZE = 40
ROWS = 20
COLS = 20

LEVEL = 1

TILE_LIST = []
button_list = []
current_tile = 0

# defining font
font = pygame.font.SysFont('Arial', 24)

# creating world_list
world_list = []
for i in range(ROWS):
    r = [-1] * COLS
    world_list.append(r)

white = (255, 255, 255)
green = (50, 200, 50)
red = (255, 0, 0)

# load bg
sky = pygame.image.load('assets\images\sky.png').convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
sun = pygame.image.load('assets\images\sun.png').convert_alpha()
sun = pygame.transform.scale(sun, (50, 50))

# draw bg

def draw_bg():
    screen.blit(sky, (0, 0))
    screen.blit(sun, (100, 100))

# draw grid

def draw_grid():
    for c in range(COLS + 1):
        pygame.draw.line(screen, white, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
    for r in range(ROWS + 1):
        pygame.draw.line(screen, white, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE))


# import tile images
dirt = pygame.image.load('assets\images\dirt.png').convert_alpha()
dirt = pygame.transform.scale(dirt, (TILE_SIZE, TILE_SIZE))

grass = pygame.image.load('assets\images\grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

platform_x = pygame.image.load('assets\images\platform_x.png').convert_alpha()
platform_x = pygame.transform.scale(platform_x, (TILE_SIZE, TILE_SIZE // 2))

platform_y = pygame.image.load('assets\images\platform_y.png').convert_alpha()
platform_y = pygame.transform.scale(platform_y, (TILE_SIZE, TILE_SIZE // 2))

blob = pygame.image.load('assets\images\\blob.png').convert_alpha()
blob = pygame.transform.scale(blob, (TILE_SIZE, int(TILE_SIZE * 0.75)))

coin = pygame.image.load('assets\images\coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (TILE_SIZE // 2, TILE_SIZE // 2))

door = pygame.image.load('assets\images\exit.png').convert_alpha()
door = pygame.transform.scale(door, (TILE_SIZE, int(TILE_SIZE * 1.5)))

lava = pygame.image.load('assets\images\lava.png').convert_alpha()
lava = pygame.transform.scale(lava, (TILE_SIZE, TILE_SIZE // 2))

guy = pygame.image.load('assets\images\guy1.png').convert_alpha()
guy = pygame.transform.scale(guy, (TILE_SIZE, TILE_SIZE * 2))

TILE_LIST = [dirt, grass, platform_x, platform_y, blob, coin, door, lava, guy]

# create buttons
col = 0  # 2 elements in a row
row = 0  # 5 columns

for tile in TILE_LIST:
    button = Button(tile, (SCREEN_WIDTH + (col * TILE_SIZE * 2 + 40)), (40 + row * 80))
    button_list.append(button)
    col += 1
    if col >= 2:
        col = 0
        row += 1

# display tiles and set the value of the tile

def draw_buttons():
    global current_tile
    for index, button in enumerate(button_list):
        if button.draw(screen):
            current_tile = index

# function to draw world

def draw_world():
    for y, rows in enumerate(world_list):
        for x, tile in enumerate(rows):
            if tile >= 0:
                if tile == 0:
                    img = dirt
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 1:
                    img = grass
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 2:
                    img = platform_x
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 3:
                    img = platform_y
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 4:
                    img = blob
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE + int(TILE_SIZE * 0.25)))
                if tile == 5:
                    img = coin
                    screen.blit(img, (x * TILE_SIZE + (TILE_SIZE // 4), y * TILE_SIZE + (TILE_SIZE // 4)))
                if tile == 6:
                    img = door
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE - (TILE_SIZE // 2)))
                if tile == 7:
                    img = lava
                    screen.blit(img, (x * TILE_SIZE, y * TILE_SIZE + (TILE_SIZE // 2)))
                if tile == 8:
                    img = guy
                    screen.blit(img, (x * TILE_SIZE, (y * TILE_SIZE) - TILE_SIZE))

# adding save and load functionality
save = pygame.image.load('assets\\buttons\save_btn.png').convert_alpha()
load = pygame.image.load('assets\\buttons\load_btn.png').convert_alpha()

save_btn = Button(save, screen.get_width() // 2 - 300, SCREEN_HEIGHT + 10)
load_btn = Button(load, screen.get_width() // 2 + 100, SCREEN_HEIGHT + 10)

# function to display text

def display_text(surface, text, font, x, y, text_color=white):
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                LEVEL += 1
            if event.key == pygame.K_DOWN:
                if LEVEL > 1:
                    LEVEL -= 1

    if build == True:
        screen.fill(green)
        draw_bg()
        draw_grid()
        draw_buttons()
        pygame.draw.rect(screen, red, button_list[current_tile].rect, 3)

        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] // TILE_SIZE
        y = mouse_pos[1] // TILE_SIZE
        if 0 <= x < COLS and 0 <= y < ROWS:
            if pygame.mouse.get_pressed()[0] == 1:
                if world_list[y][x] != current_tile:
                    world_list[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                world_list[y][x] = -1

        draw_world()

        display_text(screen, f'Level {LEVEL}', font, 10, SCREEN_HEIGHT + 10)

    folder_name = 'world_data'
    file_name = f'world_data{LEVEL}'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_path = os.path.join(folder_name, file_name)

    if save_btn.draw(screen):
        build = False
        if os.path.exists(file_path):
            print(f"'{file_path}' already exists.\nDo you want to overwrite it?")
            inp = None
            while inp not in ['Y', 'N']:
                inp = input('\tEnter Y - YES | N - NO\n\t').upper()[0]
            if inp == 'Y':
                pickle_out = open(file_path, 'wb')
                pickle.dump(world_list, pickle_out)
                pickle_out.close()
                print(f"Changes saved in '{file_path}'")
            else:
                print('Change the level to save the data')

        else:
            pickle_out = open(file_path, 'wb')
            pickle.dump(world_list, pickle_out)
            pickle_out.close()

        build = True

    if load_btn.draw(screen):
        if os.path.exists(file_path):
            pickle_in = open(file_path, 'rb')
            world_list = []
            world_list = pickle.load(pickle_in)
        else:
            print(f"ERROR!\n'{file_path}' dosen't exist")

    pygame.display.update()
    clock.tick(FPS)