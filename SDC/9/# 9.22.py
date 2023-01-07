# 9.22
import random
t=10000
m=0
while(t>0):
    a=[]
    b=0
    while(b!=6):
        b=random.randint(1,10)
        a.append(b)
        m=max(m,len(a ))
    # print(a)

    
    t-=1
print(m)