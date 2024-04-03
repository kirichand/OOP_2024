import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

circle (screen,(225,225,0), (200,200),150)
circle (screen,(0,0,0), (200,200),150,2)
circle (screen,(235, 52, 52), (250,150),25)
circle (screen,(0,0,0), (250,150),25,2)
circle (screen,(0,0,0), (250,150),10)
circle (screen,(235, 52, 52), (150,150),30)
circle (screen,(0,0,0), (150,150),10)
circle (screen,(0,0,0), (150,150),30,2)
rect(screen, (0,0,0), (135,270, 130, 25))
polygon(screen, (0,0,0), [(100,90),(200,130),(190,150),(90,110)])
polygon(screen, (0,0,0), [(210,150),(200,130),(290,110),(300,130)])






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True