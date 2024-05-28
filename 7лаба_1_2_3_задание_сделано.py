from random import randrange as rnd, choice
from tkinter import *
import math
import time
from PIL import Image, ImageTk

root = Tk()
fr=Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

class Ball(): # создание снаряда.
    def __init__(self,a,b): # a,b - координаты по х и у для перемещения сняряда с пушкой,откуда он полетит. 
        
        self.x = a
        self.y = b
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown']) # выбор цвета шарика-снаряда

        
        #global type
        self.type=choice([0,1]) # выбор типа снаряда (фото или круг)
        if self.type==1:
            self.r=10
            img = Image.open("/home/kirill/1.png").resize((2*self.r,2*self.r))  # путь к изображению
            self.photo = ImageTk.PhotoImage(img)
            self.id = canv.create_image(self.x, self.y, anchor=CENTER, image=self.photo)
            self.live=30
            
        elif self.type==0:
           self.id = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
           self.live=30
            

    def set_coords(self): # присваивание координат снаряда. в зависимости от типа стоит условие.
        if self.type==1:
          canv.coords(self.id, self.x, self.y)
          self.r
         
        elif self.type==0:
            canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)

    def move(self): # формула перемещения с учетом гравитации,по параболе.
        if self.y <= 500:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx**2 + self.vy**2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779

    def hittest(self, ob): # проверка на достижение цели снарядом. координаты снарада через self а цели через оb
        #if self.type==0:
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r+ ob.r):
            return True
        else:
            return False
        # elif self.type==1:
            """if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
                return True
                else:
                return False"""

class Bomb(): # класс описывающий бомбу. НАДО НАСТРОИТЬ УДАЛЕНИЕ БОМБЫ ПРИ КАСАНИИ С ПУШКОЙ И УДАЛЕНИЕ ПУШКИ (ПО ВОЗМОЖНОСТИ ПУШКИ УДАЛЕНИЕ)
    def __init__(self):
        self.live=1
        self.new_bomb()
    def new_bomb(self):
        color = self.color = 'orange'    
        self.id = canv.create_oval(0, 0, 0, 0,fill=color)
        x = self.x = choice([rnd(15,100),rnd(700,750)])
        y = self.y = rnd(10,50)
        r = self.r = rnd(15, 30)
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        self.ball = [x,y,r,color,dx,dy]
        return self.ball
    def move_bomb(self):
        canv.coords(self.id,self.ball[0]-self.ball[2],self.ball[1]-self.ball[2],self.ball[0]+self.ball[2],self.ball[1]+self.ball[2])
       # self.ball[0] += self.ball[4]
        self.ball[1] += self.ball[5]
        #if self.ball[0] - self.ball[2] < 0 or self.ball[0] + self.ball[2] > 400:
            #self.ball[4] = -self.ball[4]
        if self.ball[1] - self.ball[2] < 0 or self.ball[1] + self.ball[2] > 600:
            self.ball[5] = -self.ball[5]
            self.hit_bomb1()
            self.new_bomb()
    def hit_bomb1(self): # удаление цели с доски.
        self.ball=[0,0,0,'white',0,0]
        canv.coords(self.id,-100,-100,-100,-100)

    
    
    def hit_bomb(self): # удаление цели с доски.
        global id_points
        self.ball=[0,0,0,'white',0,0]
        canv.coords(self.id,-100,-100,-100,-100)
        self.points+=1        
        canv.itemconfig(id_points,text=(t1.points+t2.points+b1.points))







    
        
    

        

class Gun(): # cоздание пушки. НАДО РАЗМНОЖИТЬ ПУШКИ!
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.new_gun(10,100)
        
    def new_gun(self,a,b): #создание новой пушки
        self.id = canv.create_line(0,0,0,0, width=7)
        x = self.x = rnd(a, b)
        
        y = self.y = rnd(1, 600)
        r = self.r = rnd(1,10)
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        color = self.color = 'orange'
        self.ball = [x,y,r,color,dx,dy]
        return self.ball 




        





    def movegun(self): #перемещение пушки
        global a,b
        canv.coords(self.id,self.ball[0]-self.ball[2],self.ball[1]-self.ball[2],self.ball[0]+self.ball[2],self.ball[1]+self.ball[2])
       # self.ball[0] += self.ball[4]
        self.ball[1] += self.ball[5]
        if self.ball[0] - self.ball[2] < 0 or self.ball[0] + self.ball[2] > 400:
            self.ball[4] = -self.ball[4]
        if self.ball[1] - self.ball[2] < 0 or self.ball[1] + self.ball[2] > 600:
            self.ball[5] = -self.ball[5]
        a = self.ball[0]-self.ball[2]
        b = self.ball[1]-self.ball[2]
    
    def hittest_gun(self, ob): # проверка на достижение цели снарядом. координаты снарада через self а цели через оb
        
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - (self.y)) <= (self.r + ob.r):
            return True
        else:
            return False
        """if abs(ob.x - (self.ball[0]-self.ball[2])) <= (self.ball[2] + ob.r) and abs(ob.y - (self.ball[1]-self.ball[2])) <= (self.ball[2] + ob.r):
            return True
        else:
            return False"""

    def fire2_start(self, event): #начало стрельбы
        self.f2_on = 1

    def fire2_end(self, event): #процесс выпуска снаряда из пушки,траекория его,завершение процесса.
        global balls, bullet
        bullet += 1
        new_ball = Ball(a,b)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0): #прицеливание + растяжение пушки
        if event:
            self.an = math.atan((event.y - self.ball[1]-self.ball[2]) / (event.x - self.ball[0]-self.ball[2]))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.ball[0]-self.ball[2], self.ball[1]-self.ball[2], self.ball[0]-self.ball[2] + max(self.f2_power, 20) * math.cos(self.an), self.ball[1]-self.ball[2] + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self): #усиление скорости вылета снаряда
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

def interface(t1, t2,b1): #вывод очков за поражение цели
    global id_points
    t1.points = 0
    t2.points = 0
    b1.points = 0
    id_points = canv.create_text(30, 30, text=(t1.points + t2.points+b1.points), font='28')

class Target():  # описание цели
    def __init__(self):
        self.live = 1
        

        self.new_target()

    def new_target(self): # создание новой цели
        self.typ=choice([0,1])
        if self.typ==0:
            self.id = canv.create_oval(0, 0, 0, 0)
        else:
            self.id = canv.create_rectangle(0, 0, 0, 0)
        x = self.x = rnd(100, 780)
        y = self.y = rnd(100, 550)
        r = self.r = rnd(15, 50)
        color = self.color = 'red'
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        self.ball = [x,y,r,color,dx,dy]
        
        return self.ball 
        #canv.coords(self.id, x - r, y - r, x + r, y + r)
        #canv.itemconfig(self.id, fill=color)
   

    def moveball(self): # перемещение цели 
        canv.coords(self.id,self.ball[0]-self.ball[2],self.ball[1]-self.ball[2],self.ball[0]+self.ball[2],self.ball[1]+self.ball[2])
        canv.itemconfig(self.id,fill=self.ball[3])
        self.rand=choice([1,2])
        if self.rand==1:

            self.ball[0] += self.ball[4]
            self.ball[1] += self.ball[5]
            self.ball[2]+= self.ball[4]
            if self.ball[2]> 50 or self.ball[2] < 0:
                self.ball[2]= -self.ball[2]
            if self.ball[0] - self.ball[2] < 0 or self.ball[0] + self.ball[2] > 400:
                self.ball[4] = -self.ball[4]
            if self.ball[1] - self.ball[2] < 0 or self.ball[1] + self.ball[2] > 300:
                self.ball[5] = -self.ball[5]
        elif self.rand==2:
            self.ball[0] += self.ball[4]
            self.ball[1] += self.ball[5]
            if self.ball[0] - self.ball[2] < 0 or self.ball[0] + self.ball[2] > 800:
                self.ball[4] = -self.ball[4]
            if self.ball[1] - self.ball[2] < 0 or self.ball[1] + self.ball[2] > 600:
                self.ball[5] = -self.ball[5]


    def hit(self): # удаление цели с доски.
        self.ball=[0,0,0,'white',0,0]
        canv.coords(self.id,-100,-100,-100,-100)
        self.points+=1
        canv.itemconfig(id_points,text=(t1.points+t2.points+b1.points))


g1 = Gun()

t1 = Target()
t2 = Target()
b1 = Bomb()

bullet = 0
balls = []

screen1 = canv.create_text(400, 300, text='', font='28')
interface(t1, t2, b1)




def new_game(event=''):
    global Gun,Bomb, t1, t2,b1,g1, screen1, balls, bullet
   
   

    t1.new_target()
    t2.new_target()
    b1.new_bomb()
   
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    b1.live = 1
    
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        t1.moveball()
        t2.moveball()
        g1.movegun()
        
        b1.move_bomb()
       


        for b in balls:
            b.move()

            #условие попадания и удаление цели.
            if b.hittest(t1)and t1.live:
                t1.live = 0
                t1.hit()
                
            if b.hittest(t2)and t2.live:
                t2.live = 0
                t2.hit()
            if b.hittest(b1)and b1.live:
                b1.live = 0
                b1.hit_bomb()
            
                
            if t1.live == 0 and t2.live == 0: # and b2.live==0 and b3.live==0: 
                b1.hit_bomb1()
                '''b2.hit_bomb1()
                b3.hit_bomb1()'''
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                
            


        canv.update()
        time.sleep(0.02)
        
        g1.targetting()
        g1.power_up()
        
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
   
    root.after(750, new_game)

new_game()
mainloop()
