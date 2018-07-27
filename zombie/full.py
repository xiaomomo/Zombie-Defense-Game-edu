# -*- coding: utf-8 -*-
import pygame, random, sys, time
from pygame.locals import *

# set up some variables
windowWidth = 1024
windowHeight = 600

maxGottenPass = 2
zombie_size = 70  # includes newKindZombies
addNewZombieRate = 30

normalZombieSpeed = 2
newKindZombieSpeed = normalZombieSpeed / 2

playerMoveSpeed = 15
bulletSpeed = 10
addNewBulletSpeed = 15

textColor = (255, 255, 255)
redColor = (255, 0, 0)


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    terminate()
                if event.key == K_RETURN:
                    return


def playerHasHitZombie(playerRect, zombies):
    for z in zombies:
        if playerRect.colliderect(z['rect']):
            return True
    return False


def bulletHasHitZombie(bullets, zombie):
    for b in bullets:
        if b['rect'].colliderect(zombie['rect']):
            bullets.remove(b)
            return True
    return False


def bulletHasHitCrawler(bullets, newKindZombie):
    for b in bullets:
        if b['rect'].colliderect(newKindZombie['rect']):
            bullets.remove(b)
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('植物大战僵尸')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('grasswalk.mp3')

# set up images
playerImage = pygame.image.load('./assets/wandoushu.png')
playerRect = playerImage.get_rect()

bulletImage = pygame.image.load('./assets/wandou.png')
bulletRect = bulletImage.get_rect()

zombieImage = pygame.image.load('./assets/jiangshi.png')
newKindZombieImage = pygame.image.load('ConeheadZombieAttack.gif')

backgroundImage = pygame.image.load('./assets/beijing.png')
rescaledBackground = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

# show the "Start" screen
windowSurface.blit(rescaledBackground, (0, 0))
windowSurface.blit(playerImage, (windowWidth / 2, windowHeight - 70))
drawText('Zombie Defence', font, windowSurface, (windowWidth / 4), (windowHeight / 4))
drawText('Press Enter to start', font, windowSurface, (windowWidth / 3), (windowHeight / 3))
pygame.display.update()
waitForPlayerToPressKey()

while True:
    # set up the start of the game
    zombies = []
    newKindZombies = []
    bullets = []

    zombiesGottenPast = 0
    score = 0

    playerRect.topleft = (180, windowHeight / 2)
    moveLeft = moveRight = False
    moveUp = moveDown = False
    shoot = False

    zombieAddCounter = 0
    newKindZombieAddCounter = 0
    bulletAddCounter = 40
    pygame.mixer.music.play(-1, 0.0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True

                if event.key == K_SPACE:
                    shoot = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False

                if event.key == K_SPACE:
                    shoot = False

        # Add new zombies at the top of the screen, if needed.
        zombieAddCounter += 1
        if zombieAddCounter == addNewZombieRate:
            zombieAddCounter = 0
            zombieSize = zombie_size
            newZombie = {
                'rect': pygame.Rect(windowWidth, random.randint(10, windowHeight - zombieSize - 10), zombieSize,
                                    zombieSize),
                'surface': pygame.transform.scale(zombieImage, (zombieSize, zombieSize)),
            }

            zombies.append(newZombie)

        # Add new newKindZombies at the top of the screen, if needed.
        newKindZombieAddCounter += 1
        if newKindZombieAddCounter == addNewZombieRate:
            newKindZombieAddCounter = 0
            newKindZombiesize = zombie_size
            newCrawler = {'rect': pygame.Rect(windowWidth, random.randint(10, windowHeight - newKindZombiesize - 10),
                                              newKindZombiesize, newKindZombiesize),
                          'surface': pygame.transform.scale(newKindZombieImage, (newKindZombiesize, newKindZombiesize)),
                          }
            newKindZombies.append(newCrawler)

        # add new bullet
        bulletAddCounter += 1
        if bulletAddCounter >= addNewBulletSpeed and shoot == True:
            bulletAddCounter = 0
            newBullet = {'rect': pygame.Rect(playerRect.centerx + 10, playerRect.centery - 25, bulletRect.width,
                                             bulletRect.height),
                         'surface': pygame.transform.scale(bulletImage, (bulletRect.width, bulletRect.height)),
                         }
            bullets.append(newBullet)

        # Move the player around.
        if moveUp and playerRect.top > 30:
            # move_ip 原地移动 Rect 对象
            playerRect.move_ip(0, -1 * playerMoveSpeed)
        if moveDown and playerRect.bottom < windowHeight - 10:
            playerRect.move_ip(0, playerMoveSpeed)

        # Move the zombies down.
        for z in zombies:
            z['rect'].move_ip(-1 * normalZombieSpeed, 0)

        # Move the newKindZombies down.
        for c in newKindZombies:
            c['rect'].move_ip(-1 * newKindZombieSpeed, 0)

        # move the bullet
        for b in bullets:
            b['rect'].move_ip(1 * bulletSpeed, 0)

        # Delete zombies that have fallen past the bottom.
        for z in zombies[:]:
            if z['rect'].left < 0:
                zombies.remove(z)
                zombiesGottenPast += 1

        # Delete newKindZombies that have fallen past the bottom.
        for c in newKindZombies[:]:
            if c['rect'].left < 0:
                newKindZombies.remove(c)
                zombiesGottenPast += 1

        for b in bullets[:]:
            if b['rect'].right > windowWidth:
                bullets.remove(b)

        # check if the bullet has hit the zombie
        for z in zombies:
            if bulletHasHitZombie(bullets, z):
                score += 1
                zombies.remove(z)

        for c in newKindZombies:
            if bulletHasHitCrawler(bullets, c):
                score += 1
                newKindZombies.remove(c)

                # Draw the game world on the window.
        windowSurface.blit(rescaledBackground, (0, 0))

        # Draw the player's rectangle, rails
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie
        for z in zombies:
            windowSurface.blit(z['surface'], z['rect'])

        for c in newKindZombies:
            windowSurface.blit(c['surface'], c['rect'])

        # draw each bullet
        for b in bullets:
            windowSurface.blit(b['surface'], b['rect'])

        # Draw the score and how many zombies got past
        drawText('zombies gotten past: %s' % (zombiesGottenPast), font, windowSurface, 10, 20)
        drawText('score: %s' % (score), font, windowSurface, 10, 50)

        # update the display
        pygame.display.update()

        # Check if any of the zombies has hit the player.
        if playerHasHitZombie(playerRect, zombies):
            break
        if playerHasHitZombie(playerRect, newKindZombies):
            break

        # check if score is over MAXGOTTENPASS which means game over
        if zombiesGottenPast >= maxGottenPass:
            break

        mainClock.tick(60)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()
    time.sleep(1)
    if zombiesGottenPast >= maxGottenPass:
        windowSurface.blit(rescaledBackground, (0, 0))
        windowSurface.blit(playerImage, (windowWidth / 2, windowHeight - 70))
        drawText('score: %s' % (score), font, windowSurface, 10, 30)
        drawText('GAME OVER', font, windowSurface, (windowWidth / 3), (windowHeight / 3))
        drawText('YOUR COUNTRY HAS BEEN DESTROIED', font, windowSurface, (windowWidth / 4) - 80,
                 (windowHeight / 3) + 100)
        drawText('Press enter to play again or escape to exit', font, windowSurface, (windowWidth / 4) - 80,
                 (windowHeight / 3) + 150)
        pygame.display.update()
        waitForPlayerToPressKey()
    if playerHasHitZombie(playerRect, zombies):
        windowSurface.blit(rescaledBackground, (0, 0))
        windowSurface.blit(playerImage, (windowWidth / 2, windowHeight - 70))
        drawText('score: %s' % (score), font, windowSurface, 10, 30)
        drawText('GAME OVER', font, windowSurface, (windowWidth / 3), (windowHeight / 3))
        drawText('YOU HAVE BEEN KISSED BY THE ZOMMBIE', font, windowSurface, (windowWidth / 4) - 80,
                 (windowHeight / 3) + 100)
        drawText('Press enter to play again or escape to exit', font, windowSurface, (windowWidth / 4) - 80,
                 (windowHeight / 3) + 150)
        pygame.display.update()
        waitForPlayerToPressKey()
    gameOverSound.stop()
