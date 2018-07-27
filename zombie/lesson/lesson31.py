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

zombieRect = zombieImage.get_rect()

backgroundImage = pygame.image.load('../assets/beijing.png')
rescaledBackground = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

windowSurface.blit(rescaledBackground, (0, 0))
windowSurface.blit(playerImage, (200, 80))
windowSurface.blit(zombieImage, (800, 100))
pygame.display.update()

zombieRect.topleft = (800, 100)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.blit(rescaledBackground, (0, 0))
    windowSurface.blit(playerImage, (200, 80))

    zombieRect.move_ip(-2, 0)
    windowSurface.blit(zombieImage, zombieRect)

    pygame.display.update()
