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
bulletImage = pygame.image.load('../assets/wandou.png')

bulletInitLocation = (250, 90)
zombieInitLocation = (800, 100)
speed = 5

windowSurface.blit(rescaledBackground, (0, 0))
windowSurface.blit(playerImage, (200, 80))
windowSurface.blit(zombieImage, zombieInitLocation)
windowSurface.blit(bulletImage, bulletInitLocation)
pygame.display.update()

zombieRect = zombieImage.get_rect()
zombieRect.topleft = zombieInitLocation
bulletRect = bulletImage.get_rect()
bulletRect.topleft = bulletInitLocation

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.blit(rescaledBackground, (0, 0))
    windowSurface.blit(playerImage, (200, 80))

    zombieRect.move_ip(-speed, 0)
    windowSurface.blit(zombieImage, zombieRect)

    bulletRect.move_ip(speed, 0)
    windowSurface.blit(bulletImage, bulletRect)

    pygame.display.update()
