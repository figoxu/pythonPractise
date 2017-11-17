# -*- coding: UTF-8 -*-

import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Audio")

WHITE = (255,255,255)

screen.fill(WHITE)

sound = pygame.mixer.Sound('resources/bounce.ogg')
sound.play()

pygame.mixer.music.load('resources/bgmusic.mp3')
# 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
pygame.mixer.music.play(-1,0.0)

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    pygame.display.update()
