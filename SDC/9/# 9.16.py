# 9.16
import random
t=3
s=0
while(t>0):
    if(s>200):
        break
    a=random.randint(2,99)
    b=random.randint(2,99)
    print(a,b)
    # print(a*b)
    c=int(input())
    if(c==a*b):
        s+=a+b
        print("correct")
        print(s)
        print(t)
    else:
        t-=1
        print("wrong")
        print(s)
        print(t)
        
    
