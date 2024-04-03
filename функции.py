import random
import _random


def func (chislo):
    q=0
    o=0
    
    list = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range (0,len(list)):
        for j in range(0,len(list[i])):
           
           list[i][j] = random.randint(1,50)
           if list[i][j-1]==list[i][j] or list[i-1][j]==list[i][j] or list[i-1][j-1]==list[i][j]:
               list[i][j] = random.randint(1,50)

        list[i].sort()
    list.sort()

    N = len(list)
    M = len(list[0])

    i=0
    j=4
    while o==0:
        q+=1
        if list[i][j]==chislo:
            print ("Число найдено за ", q, "итераций")
            break
        elif list[i][j]<chislo:
            if (i >= N-1):
                break
            i+=1
        elif list[i][j]>chislo:
            if j <= 0:
                break
            j-=1

   
    
            
             
    print(list)

    

func(45)




