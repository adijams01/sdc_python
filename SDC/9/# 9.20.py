# 9.20
import random
n=int(input())
i=1
a=[]
while(i!=n):
    b=random.randint(0,n)
    print(i,".",b)
    try:
        if(a.index(b)>=0):
            break
   
    except ValueError:
        a.append(b)
    # print(a)
    
    i+=1