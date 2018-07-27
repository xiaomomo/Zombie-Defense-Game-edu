import pygame, sys
from pygame.locals import *

windowWidth = 1024
windowHeight = 600

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('植物大战僵尸')

# set up images
playerImage = pygame.image.load('../assets/wandoushu.png')
playerRect = playerImage.get_rect()

bulletImage = pygame.image.load('../assets/wandou.png')

zombieImage = pygame.image.load('../assets/zombie.png')
hatKindZombieImage = pygame.image.load('../assets/hatZombie.gif')

backgroundImage = pygame.image.load('../assets/beijing.png')
rescaledBackground = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

windowSurface.blit(rescaledBackground, (0, 0))
windowSurface.blit(playerImage, (200, 80))
windowSurface.blit(zombieImage, (800, 100))
windowSurface.blit(hatKindZombieImage, (800, 300))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
