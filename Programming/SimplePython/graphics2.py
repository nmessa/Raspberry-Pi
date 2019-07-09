# graphics

import pygame, time, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("graphics example")
black = pygame.Color(0, 0, 0)
red   = pygame.Color(255, 0, 0)

def draw():
    screen.fill(black)

    for a in range(0,300):
        x = random.randrange(1,50)
        y = random.randrange(1,50)
        pygame.draw.rect(screen, red, Rect(x*10, y*10, 10, 10))

    pygame.display.flip()

while True:
    draw()
    fpsClock.tick(30)
