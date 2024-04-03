import pygame
from pygame.draw import *
from random import randint,choice




pygame.init()

FPS = 30
shirina, vysota = 1200,900
screen = pygame.display.set_mode((shirina,vysota))

# Цвета шариков
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLORS = [RED,BLUE,YELLOW,GREEN,MAGENTA,CYAN]

# Кол-во шариков
NUM_BALLS = 10
balls = []


# Очки
score = 0

def new_ball():
    '''Создает новый шарик со случайными параметрами.'''
    x = randint(100,1100)
    y = randint(100,900)
    r = randint(10,100)
    color = choice(COLORS)
    dx,dy = randint(-5,5),randint(-5,5)
    return [x,y,r,color,dx,dy]

def draw_ball(ball):
    '''Рисует шарик на экране.'''
    circle(screen,ball[3],(ball[0],ball[1]),ball[2])

def move_ball(ball):
    '''Обновляет положение шарика, учитывая столкновения со стенами.'''
    ball[0] += ball[4]
    ball[1] += ball[5]
    if ball[0] - ball[2] < 0 or ball[0] + ball[2] > shirina:
        ball[4] = -ball[4]
    if ball[1] - ball[2] < 0 or ball[1] + ball[2] > vysota:
        ball[5] = -ball[5]

def check_click(event,ball):
    '''Проверяет, попал ли клик в шарик.'''
    result = ((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)**0.5
    return result < ball[2]

# Создаем начальные шарики
for _ in range(NUM_BALLS):
    balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if check_click(event,ball):
                    score += 1
                    print(f"Очки: {score}")
                    balls.remove(ball)
                    balls.append(new_ball())

    screen.fill(WHITE)
    for ball in balls:
        draw_ball(ball)
        move_ball(ball)
    pygame.display.update()

pygame.quit()



