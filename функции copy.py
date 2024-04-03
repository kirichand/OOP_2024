import random
import _random


def func (chislo,stb,str):
    q=0
    o=0
    list1 = []
    list = [[1]*str for i in range(stb)]
    for i in range (0,len(list)):
        for j in range(0,len(list[i])): 
            if i==0 and j!=0:
                while o==0:
                    c=list[i][j-1]+random.randint(1,10)
                    if not c in list1:
                        list1.append(c)
                        list[i][j] = c
                        break

            elif i!=0 and j==0:
                while o==0:
                    c=list[i-1][j]+random.randint(1,10)
                    if not c in list1:
                        list1.append(c)
                        list[i][j] = c
                        break

            elif i!=0 and j!=0:
                while o==0:
                    c=max(list[i-1][j],list[i][j-1])+random.randint(1,10)
                    if not c in list1:
                        list1.append(c)
                        list[i][j] = c
                        break
                
        
               
               

       

    N = len(list)
    M = len(list[0])

    i=0
    j=str-1
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
   


    for i in range(len(list)):
        for j in range (len(list[i])):
            if list[i][j]<10:
                print('', list[i][j], end = ' ')
            else:
                print(list[i][j], end = ' ')
        print('')
    



   
    
            
             
   
print("Введите кол-во строк:", end = '')
str=int(input())
print("Введите кол-во столбцов:", end = '')
stb=int(input())
print ("Введите число от 1 до 50")
chislo = int(input ())
func(chislo,str,stb)




