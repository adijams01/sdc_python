# 9.8
import random
t=1
while(t<20 or t>100):
    print("enter no. (20-100)")
    t=int(input())
while(t>0):
    t-=random.randint(1,10)
    print(t,end=" ")
    