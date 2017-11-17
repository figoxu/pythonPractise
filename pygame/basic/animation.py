# -*- coding: UTF-8 -*-

import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Animation")

img = pygame.image.load('resources/img.png')
imgx,imgy,direction = 10,10,'right'

WHITE = (255,255,255)
while True:
    screen.fill(WHITE)
    if direction=='right':
        imgx += 5
        if imgx == 380 :
            direction ='down'
    elif direction=='down':
        imgy += 5
        if imgy == 300 :
            direction='left'
    elif direction=='left':
        imgx -=5
        if imgx == 10:
            direction='up'
    elif direction=='up':
        imgy -=5
        if imgy == 10:
            direction='right'

    screen.blit(img,(imgx,imgy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()
    pygame.display.update()

