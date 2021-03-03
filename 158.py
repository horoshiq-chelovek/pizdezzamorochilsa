import pygame
import random
main = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
W = 640
H = 480
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
s = 50
y_vector = 0
x_vector = 0
keys = 0
while main == True:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    if y > 480 - s:
        y = 480 -s
        y_vector = 0
    if x > 640 - s:
        x = 640 - s
        x_vector = 0
    if x < s:
        x = s
        x_vector = 0
    y_vector += 1
    if x_vector > 0:
        x_vector -= 1
    if x_vector < 0:
        x_vector += 1
    y += y_vector
    x += x_vector
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_vector += 10
            if event.key == pygame.K_LEFT:
                x_vector -= 0
            if event.key == pygame.K_UP:
                y_vector -= 30
    #render
    screen.fill((100,100,100))
    pygame.draw.circle(screen,(255,255,255),(x,y),s)
    pygame.draw.rect(screen, (255, 0, 0), (x-50, y-s-20, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0),(x-50, y-s-20, hp, 10))

    pygame.display.flip()