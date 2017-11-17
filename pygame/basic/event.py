# -*- coding: UTF-8 -*-

import pygame,sys
from pygame.locals import *
from math import pi

pygame.init()

WHITE=(255,255,255)
screen = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Event")
screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            print(event.pos)

        # 获得鼠标按下的位置
        if event.type == MOUSEBUTTONDOWN:
            print("鼠标按下：", event.pos)

        # 获得鼠标抬起的位置
        if event.type == MOUSEBUTTONUP:
            print("鼠标抬起：", event.pos)
        if event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w):
                print("上")
            if (event.key == K_DOWN or event.key == K_s):
                print("下")
            if (event.key == K_LEFT or event.key == K_a):
                print("左")
            if (event.key == K_RIGHT or event.key == K_d):
                print("右")
            # 按下键盘的Esc键退出
            if (event.key == K_ESCAPE):
                # 退出pygame
                pygame.quit()
                # 退出系统
                sys.exit()

    pygame.display.update()