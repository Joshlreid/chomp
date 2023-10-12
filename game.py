import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")

screen.fill((155, 0, 255))
pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400))
pygame.draw.rect(screen, (0,170,0), (300, 75, 75, 75))


pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("no today! this games runs 4eva")