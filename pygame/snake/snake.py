# -*- coding: UTF-8 -*-

import random,sys,time,pygame
from pygame.locals import *

FPS,WINDOWWIDTH,WINDOWHEIGHT,CELLSIZE = 5,640,680,20

assert WINDOWWIDTH % CELLSIZE ==0,"Window Width Must Be A Multiple Of Cell Size"
assert WINDOWHEIGHT % CELLSIZE == 0,"Window Height Must Be A Multiple Of Cell Size"

CELLWIDTH,CELLHEIGHT = int(WINDOWWIDTH/CELLSIZE),int(WINDOWHEIGHT/CELLSIZE)

WHITE,BLACK,RED =(255,255,255),(0,0,0),(255,0,0)
GRENN,DARKGREEN,DARKGRAY=(0,255,0),(0,155,0),(40,40,40)
BGCOLOR = BLACK

UP,DOWN,LEFT,RIGHT='up','down','left','right'

HEAD=0

def main():

    global FPSCLOCK,DISPLAYSURF,BASICFONT

    pygame.init()
    FPSCLOCK,DISPLAYSURF,BASICFONT = pygame.time.Clock(),pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)),pygame.font.Font("resources/ARBERKLEY.ttf")
    pygame.display.set_caption("Snake")



def showStartScreen():
    DISPLAYSURF.fill(BGCOLOR)
    titleFont = pygame.font.Font("resources/ARBERKLEY.ttf",100)
    titleSurf = titleFont.render('Snake!',True,GRENN)
    titleRect= titleSurf.get_rect()
    titleRect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)




