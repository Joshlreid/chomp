import pygame
import sys
import random
import fish
from settings import *
import minnow

pygame.init()

# fonts
game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 80)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass.set_colorkey((0, 0, 0))

# create a new fish
my_fish = fish.Fish(200, 200)
my_minnows = []

for _ in range(NUM_MINNOWS):
    my_minnows.append(minnow.Minnow(random.randint(0, SCREEN_WIDTH-TILE_SIZE),
                                    random.randint(0, WATER_BOTTOM-TILE_SIZE)))

background = screen.copy()
clock = pygame.time.Clock()


def draw_background():
    # draw water
    background.fill(WATER_COLOR)

    # blit sand tiles across the bottom of the
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
        background.blit(sand_top, (TILE_SIZE * i, (SCREEN_HEIGHT - (2 * TILE_SIZE))))

    # randomly place 4 pieces of grass along the bottom of the screen
    for _ in range(4):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
        background.blit(seagrass, (x, y))

    # drawing font
    text = game_font.render("Chomp!", True, (255, 69, 0))
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                           SCREEN_HEIGHT // 2 - text.get_height() // 2))


draw_background()

while True:
    # listen for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thank fo play")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
                print('left arrow pressed!')
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
                print('right arrow pressed!')
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
                print('left arrow pressed!')
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
                print('right arrow pressed!')
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False


# update the game screen
    my_fish.update()
    for my_minnow in my_minnows:
        my_minnow.update()

# draw the game screen
    screen.blit(background, (0, 0))
    my_fish.draw(screen)
    for my_minnow in my_minnows:
        my_minnow.draw(screen)
    pygame.display.flip()
    clock.tick(60)