#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Snake for Android  (Pydroid 3)
在手机上直接运行的贪吃蛇
手势：上下左右轻扫控制方向
点击屏幕重新开始
"""

import random

import pygame

pygame.init()
# ---------- 基本参数 ----------
W, H = 480, 640  # 画布大小（px）
CELL = 24  # 格子大小（px）
COL, ROW = W // CELL, H // CELL
FPS = 12
FONT = pygame.font.SysFont('arial', 32)

# ---------- 颜色 ----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 30, 30)
GRAY = (40, 40, 40)

# ---------- 屏幕 ----------
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("贪吃蛇 - Windows 版")
clock = pygame.time.Clock()


# ---------- 游戏对象 ----------
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        # 初始 3 节，向右
        x = COL // 2
        self.body = [(x, ROW // 2), (x - 1, ROW // 2), (x - 2, ROW // 2)]
        self.dir = (1, 0)
        self.alive = True

    def head(self):
        return self.body[0]

    def turn(self, dxdy):
        # 禁止 180° 掉头
        if (dxdy[0] * -1, dxdy[1] * -1) != self.dir:
            self.dir = dxdy

    def move(self):
        if not self.alive:
            return
        hx, hy = self.head()
        dx, dy = self.dir
        nx, ny = (hx + dx) % COL, (hy + dy) % ROW  # 穿墙
        # 撞自己
        if (nx, ny) in self.body:
            self.alive = False
            return
        self.body.insert(0, (nx, ny))
        # 吃到食物
        if (nx, ny) == food.pos:
            food.spawn()
        else:
            self.body.pop()


class Food:
    def spawn(self):
        self.pos = (random.randint(0, COL - 1), random.randint(0, ROW - 1))
        # 避免刷在蛇身上
        while self.pos in snake.body:
            self.pos = (random.randint(0, COL - 1), random.randint(0, ROW - 1))


# ---------- 实例 ----------
snake = Snake()
food = Food()
food.spawn()


# ---------- 输入（键盘/鼠标） ----------
def handle_input(ev):
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_RIGHT:
            dx, dy = snake.dir
            snake.turn((-dy, dx))  # 顺时针
        elif ev.key == pygame.K_LEFT:
            dx, dy = snake.dir
            snake.turn((dy, -dx))  # 逆时针
        elif ev.key in (pygame.K_SPACE, pygame.K_r):
            if not snake.alive:
                snake.reset()
                food.spawn()
    elif ev.type == pygame.MOUSEBUTTONUP:
        if not snake.alive:
            snake.reset()
            food.spawn()


# ---------- 主循环 ----------
while True:
    # 事件
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit();
            exit()
        handle_input(ev)

    # 逻辑
    snake.move()

    # 绘制
    screen.fill(GRAY)
    # 网格
    for x in range(COL):
        pygame.draw.line(screen, BLACK, (x * CELL, 0), (x * CELL, H))
    for y in range(ROW):
        pygame.draw.line(screen, BLACK, (0, y * CELL), (W, y * CELL))
    # 蛇
    for idx, (x, y) in enumerate(snake.body):
        color = GREEN if idx == 0 else (0, 180, 0)
        pygame.draw.rect(screen, color, (x * CELL + 2, y * CELL + 2, CELL - 4, CELL - 4))
    # 食物
    fx, fy = food.pos
    pygame.draw.ellipse(screen, RED, (fx * CELL + 2, fy * CELL + 2, CELL - 4, CELL - 4))

    # 分数 / 提示
    msg = f"分数: {len(snake.body) * 10}"
    if not snake.alive:
        msg += "  —— 按空格/R 或鼠标点击重新开始"
    else:
        msg += "  （左右方向键转向）"
    txt = FONT.render(msg, True, WHITE)
    screen.blit(txt, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
