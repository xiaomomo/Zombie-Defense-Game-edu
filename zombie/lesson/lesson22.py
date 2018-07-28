import pygame, sys
from pygame.locals import *

windowWidth = 1024
windowHeight = 600

pygame.init()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('植物大战僵尸')

# set up images
playerImage = pygame.image.load('../assets/wandoushu.png')
zombieImage = pygame.image.load('../assets/zombie.png')

backgroundImage = pygame.image.load('../assets/beijing.png')
rescaledBackground = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

windowSurface.blit(rescaledBackground, (0, 0))
windowSurface.blit(playerImage, (200, 80))
windowSurface.blit(zombieImage, (800, 100))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
