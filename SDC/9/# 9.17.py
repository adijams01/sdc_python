# 9.17
import random
t=10
c=50
while(t>1):
    b=random.randint(1,t)
    # print(b)
    a=int(input())
    if(a==b):
        c*=2
        t-=1
        print("correct")
        print(c)
    elif(a==0):
        print("quit")
        break
        
    else:
        print("incorrect lost")
        break

    
if(t==1):
    print("win")