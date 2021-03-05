import pygame as pg
import pygame
import sys
from pygame.locals import *
import random
main = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
W = 1200
H = 800
FPS = 60
key = 0
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Lox")
clock = pygame.time.Clock()
hp = 100
hp_max = 100
ki =100
ki_max = 100
x = 60
y = 60
s = 20
y_vector = 0
x_vector = 0
x_cam = 0
y_cam = 0
jump_c = 0
storona = 0
fly = 0
char = 'loks.png'
player = pygame.image.load(char).convert_alpha()
keys = 0
#bloki   [x,y,png_file,hp_max,hp]
bloks_vran = []
bloks = [[2,2,'resu/dirt.png',50,50]]
blok = 0
#ki      [x,y,[r,g,b],damage]
attacks = []
while main == True:
    print(y_vector)
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    if fly == 1:
        ki -= 0
        y_vector -= 1
        if y_vector > 0:
            y_vector -= 1
        if y_vector < -1:
            y_vector += 1
    if y > H - s:
        y = H -s
        jump_c = 1
        if y_vector > 35:
            hp -= y_vector -30
        y_vector = 0
    if x > W - s:
        x = W - s
        x_vector = 0
    if x < s:
        x = s
        x_vector = 0
    y_vector += 1
    if x_vector > 0:
        x_vector -= 1
    if x_vector < 0:
        x_vector += 1
    #yprovlenie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jump_c > 0:
                    y_vector -= 10
                    jump_c = 0
            if event.key == pygame.K_f:
                if fly == 0:
                    fly = 1
                else:
                    fly = 0
    if key[pygame.K_a]:
        storona = 1
        x_vector -= 2
        if x_vector < -10:
            x_vector = -10
    if key[pygame.K_d]:
        storona = 0
        x_vector += 2
        if x_vector > 10:
            x_vector = 10
    if key[pygame.K_w]:
        if fly == 1:
            y_vector -= 2
            if y_vector < -10:
                y_vector = -10
    if key[pygame.K_s]:
        if fly == 1:
            y_vector += 2
            if y_vector > 10:
                y_vector = 10
    y += y_vector
    x += x_vector
    #render===================
    screen.fill((100,100,100))
    pygame.draw.circle(screen, (210, 210, 210), (60, 60), 60)
    #world==========================
    idc = 0
    while idc < len(bloks):
        char = pygame.image.load(bloks[idc][2]).convert_alpha()
        screen.blit(char,(bloks[idc][0]*50,bloks[idc][1]*50))
        idc += 1
    #----character
    pygame.draw.circle(screen,(210,210,210),(x,y),s)
    if storona == 0:
        pygame.draw.circle(screen, (0, 0, 0), (x+s*0.5, y-s*0.5), s/10)
    if storona == 1:
        pygame.draw.circle(screen, (0, 0, 0), (x-s*0.5, y-s*0.5), s/10)
    pygame.draw.rect(screen, (255, 0, 0), (x-50, y-s-25, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0),(x-50, y-s-25, hp//(hp_max/100), 10))
    pygame.draw.rect(screen, (255, 0, 0),(x-50, (y-s-10), 100, 10))
    pygame.draw.rect(screen, (0, 100, 255),(x-50, y-s-10, ki//(ki_max/100), 10))
    #koneq=======
    pygame.display.flip()