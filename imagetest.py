import pygame
from pygame.locals import*
img = pygame.image.load('clouds.bmp')

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()