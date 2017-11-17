# -*- coding: UTF-8 -*-

import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,400))

pygame.display.set_caption('Font')

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)

fontObj = pygame.font.Font('resources/ARBERKLEY.ttf',50)

textSurfaceObj = fontObj.render('FigoXu@Pygame',True,BLUE,GREEN)

textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250,250)
screen.fill(WHITE)

screen.blit(textSurfaceObj,textRectObj)

while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    pygame.display.update()