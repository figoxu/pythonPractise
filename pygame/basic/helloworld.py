# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,400))

pygame.display.set_caption('Hello World')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()