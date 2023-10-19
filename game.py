import pygame
import sys
import random

from settings import *

pygame.init()

# fonts
game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 80)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()

# blit sand tiles across the bottom of the screen
sand_top.set_colorkey((0, 0, 0))
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand, (TILE_SIZE*i, SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE*i, (SCREEN_HEIGHT - (2*TILE_SIZE))))

# randomly place 4 pieces of grass along the bottom of the screen
seagrass.set_colorkey((0,0,0))
for _ in range(4):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(SCREEN_HEIGHT - 2*TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
    screen.blit(seagrass, (x,y))

# drawing font
text = game_font.render("Chomp!", True, (255, 69, 0))
screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2,
                   SCREEN_HEIGHT//2 - text.get_height()//2))


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thank fo play")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
