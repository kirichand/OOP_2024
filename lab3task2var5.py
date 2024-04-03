import pygame
import numpy
from pygame.draw import *
import math as m





def ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
pygame.init()
FPS = 30
screen = pygame.display.set_mode((1000, 800))
rect(screen, (220,220,220), (0,0, 1000, 800))
rect(screen, (255,255,255 ), (0,400, 1000, 400))


def Iglu (x,y,r): #x,y - coordinates; r - масштаб
    arc(screen, (220,220,220), (100*r+x,300*r+y,400*r,300*r), 0, m.pi,10000)
    arc(screen, (0,0,0), (100*r+x,300*r+y,400*r,300*r), 0, m.pi,2)
    line(screen,(0,0,0),((100*r+x),(450*r+y)),((500*r+x),(450*r+y)),1)
    line(screen,(0,0,0),((115*r+x),(400*r+y)),((485*r+x),(400*r+y)),1)
    line(screen,(0,0,0),(150*r+x,350*r+y),(450*r+x,350*r+y),1)
    line(screen,(0,0,0),(200*r+x,320*r+y),(400*r+x,320*r+y),1)
    line(screen,(0,0,0),(300*r+x,320*r+y),(300*r+x,350*r+y),1)
    line(screen,(0,0,0),(210*r+x,320*r+y),(200*r+x,350*r+y),1)
    line(screen,(0,0,0),(380*r+x,320*r+y),(390*r+x,350*r+y),1)
    line(screen,(0,0,0),(310*r+x,300*r+y),(300*r+x,320*r+y),1)
    line(screen,(0,0,0),(220*r+x,400*r+y),(230*r+x,350*r+y),1)
    line(screen,(0,0,0),(160*r+x,400*r+y),(180*r+x,350*r+y),1)
    line(screen,(0,0,0),(160*r+x,400*r+y),(180*r+x,350*r+y),1)
    line(screen,(0,0,0),(320*r+x,400*r+y),(310*r+x,350*r+y),1)
    line(screen,(0,0,0),(400*r+x,400*r+y),(380*r+x,350*r+y),1)
    line(screen,(0,0,0),(160*r+x,450*r+y),(180*r+x,400*r+y),1)
    line(screen,(0,0,0),(160*r+x,450*r+y),(180*r+x,400*r+y),1)
    line(screen,(0,0,0),(160*r+x,450*r+y),(180*r+x,400*r+y),1)
    line(screen,(0,0,0),(120*r+x,450*r+y),(140*r+x,400*r+y),1)
    line(screen,(0,0,0),(255*r+x,450*r+y),(270*r+x,400*r+y),1)
    line(screen,(0,0,0),(360*r+x,450*r+y),(345*r+x,400*r+y),1)
    line(screen,(0,0,0),(440*r+x,450*r+y),(425*r+x,400*r+y),1)

def Cat (x,y,r):
    ellipse(screen,(220,220,220),(200*r+x,600*r+y,200*r,30*r))
    ellipse(screen,(220,220,220),(190*r+x,580*r+y,60*r,30*r))
    ellipse_angle(screen,(220,220,220),(140*r+x,620*r+y,100*r,15*r),15)
    ellipse_angle(screen,(220,220,220),(160*r+x,630*r+y,100*r,15*r),25)
    ellipse_angle(screen,(220,220,220),(365*r+x,620*r+y,100*r,15*r),-15)
    ellipse_angle(screen,(220,220,220),(350*r+x,635*r+y,100*r,15*r),-25)
    ellipse_angle(screen,(220,220,220),(370*r+x,590*r+y,100*r,15*r),25)
    ellipse_angle(screen,(255,255,255),(192*r+x,585*r+y,10*r,10*r),25)
    ellipse_angle(screen,(255,255,255),(210*r+x,585*r+y,10*r,10*r),25)
    ellipse_angle(screen,(0,0,0),(198*r+x,588*r+y,5*r,5*r),25)
    ellipse_angle(screen,(0,0,0),(218*r+x,588*r+y,5*r,5*r),25)
    ellipse_angle(screen,(0,0,0),(198*r+x,598*r+y,3*r,3*r),25)
    polygon(screen,(220,220,220),[(205*r+x,585*r+y),(212*r+x,570*r+y),(219*r+x,580*r+y),(205*r+x,585*r+y)])
    polygon(screen,(220,220,220),[(225*r+x,585*r+y),(232*r+x,570*r+y),(242*r+x,590*r+y),(225*r+x,585*r+y)])
    ellipse_angle(screen,(163, 153, 196),(165*r+x,605*r+y,75*r,15*r),-25)
    polygon(screen,(163, 153, 196),[(225*r+x,620*r+y),(240*r+x,635*r+y),(245*r+x,625*r+y),(225*r+x,620*r+y)])
    circle(screen,(255,255,255),(175*r+x,599*r+y),5*r)
    circle(screen,(0,0,0),(175*r+x,599*r+y),5*r,1)
    circle(screen,(0,0,0),(175*r+x,599*r+y),2*r)
   


def Chuckcha (x,y,r):
   
    arc(screen, (140, 105, 83), (750*r+x,500*r+y,200*r,200*r), 0, m.pi,100000)
    ellipse_angle(screen,(140, 105, 83),(750*r+x,580*r+y,100*r,60*r),-90)
    ellipse_angle(screen,(140, 105, 83),(850*r+x,580*r+y,100*r,60*r),-90)
    ellipse_angle(screen,(140, 105, 83),(750*r+x,630*r+y,80*r,30*r),-180)
    ellipse_angle(screen,(140, 105, 83),(870*r+x,630*r+y,80*r,30*r),0)
    ellipse_angle(screen,(140, 105, 83),(695*r+x,510*r+y,100*r,30*r),190)
    ellipse_angle(screen,(140, 105, 83),(895*r+x,510*r+y,100*r,30*r),-10)
    polygon(screen,(77, 53, 12),[(750*r+x,600*r+y),(750*r+x,620*r+y),(950*r+x,620*r+y),(950*r+x,600*r+y)])
    polygon(screen,(77, 53, 12),[(825*r+x,600*r+y),(875*r+x,600*r+y),(875*r+x,500*r+y),(825*r+x,500*r+y)])
    circle(screen,(196, 185, 177),(850*r+x,450*r+y),80*r)
    circle(screen,(145, 95, 60),(850*r+x,450*r+y),60*r)
    circle(screen,(230, 199, 177),(850*r+x,450*r+y),40*r)
    line(screen,(0,0,0),(700*r+x,450*r+y),(720*r+x,600*r+y),3)
    line(screen,(0,0,0),(825*r+x,430*r+y),(840*r+x,435*r+y),1)
    line(screen,(0,0,0),(875*r+x,430*r+y),(860*r+x,435*r+y),1)
    line(screen,(0,0,0),(825*r+x,470*r+y),(840*r+x,465*r+y),1)
    line(screen,(0,0,0),(840*r+x,465*r+y),(860*r+x,465*r+y),1)
    line(screen,(0,0,0),(860*r+x,465*r+y),(875*r+x,470*r+y),1)
  

Iglu(400,200,0.5)
Iglu(400,300,0.5)
Iglu(0,0,1)


Cat(0,0,1)
Cat(200,200,0.5)
Chuckcha(0,0,1)
Chuckcha(50,300,0.5)
Chuckcha(80,400,0.5)










pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

