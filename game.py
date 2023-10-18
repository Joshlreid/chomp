import pygame
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64

# COLORS
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")

screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH / 2 - TILE_SIZE / 2, SCREEN_HEIGHT / 2 - TILE_SIZE / 2))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thank fo play")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
