# graphics

import pygame, time, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("graphics example")
black = pygame.Color(0, 0, 0)
red   = pygame.Color(255, 0, 0)

screen.fill(black)

pygame.draw.rect(screen, red, Rect(10, 10, 20, 20))
pygame.display.flip()

while True:
    print ("waiting")
    fpsClock.tick(20)
    time.sleep(1)

