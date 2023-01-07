# 9.15
import random
t=100
while(t>0 and t<200):
    b=random.randint(0,10)
    a=int(input())
    if(a==b):
        t+=100
    elif(abs(a-b)>4):
        t-=20
    else:
        t-=10
    print(b)
    print(t)
if(t>=200):
    print(t,"win")
else:
    print(t,"lose")