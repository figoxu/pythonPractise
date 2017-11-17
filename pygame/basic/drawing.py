# -*- coding: UTF-8 -*-
# drawing.py

# 导入需要的模块
import pygame, sys
from pygame.locals import *
from math import pi


# 初始化pygame
pygame.init()

# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((400,300))

# 设置窗口标题
pygame.display.set_caption('Drawing')

# 定义颜色
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# 设置背景颜色
screen.fill(WHITE)

# 绘制一条线
pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)

# 绘制一条抗锯齿的线
pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80],True)

# 绘制一条折线
pygame.draw.lines(screen, BLACK, False, 
                  [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

# 绘制一个空心矩形
pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

# 绘制一个矩形
pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

# 绘制一个空心椭圆
pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

# 绘制一个椭圆
pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

# 绘制多边形
pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

# 绘制多条弧线
pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3*pi/2, 2*pi, 2)

# 绘制一个圆
pygame.draw.circle(screen, BLUE, [60, 250], 40)

# 程序主循环
while True:

    # 获取事件
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()

    # 绘制屏幕内容
    pygame.display.update()