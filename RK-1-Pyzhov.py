
import random
import _random


def func (chislo):
    q=0

    
    list = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range (0,len(list)):
        for j in range(0,len(list[i])):
           
           list[i][j] = random.randint(1,50)
           if list[i][j-1]==list[i][j] or list[i-1][j]==list[i][j] or list[i-1][j-1]==list[i][j]:
               list[i][j] = random.randint(1,50)

        list[i].sort()
    list.sort() 
    for i in list:
        for j in i:
            q+=1
            if j==chislo:
                True
                print ("Число найдено за ", q, "итераций")
    
            
             
    print(list)

    return list

func(45)






