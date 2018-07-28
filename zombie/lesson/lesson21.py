import pygame, sys
from pygame.locals import *

windowWidth = 1024
windowHeight = 600

pygame.init()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

backgroundImage = pygame.image.load('../assets/beijing.png')
rescaledBackground = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

windowSurface.blit(rescaledBackground, (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
