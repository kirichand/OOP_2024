import pygame 
from pygame.draw import *
import math
FPS = 30
screen = pygame.display.set_mode((400, 400))
x=0
y=0
s=0
w=0

def proverka (a,b,c,d):
    if c-a==0 or d-b==0 or c-a!=10 or d-b!=10:
        print('Введите корректные значения x2 и y2!')
        return False
    else:
        circle (screen,(255,0,0),(a+5,b+5),5)
        circle (screen,(255,0,0),(c+5,d+5),5)

rect (screen,(255,255,255),(0,0,400,400))
for i in range (180):
   for j in range(100):
        rect(screen,(0,0,0),(i*10,j*10,10,10),1)
        
a = int(input('Ввод x1:'))*10
b = int(input('Bвод y1:'))*10
c = int(input('Ввод x2:'))*10 
d = int(input('Bвод y2:'))*10

proverka(a,b,c,d)

























































pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()