# 7.25
import random
t=10000
c=0
while(t>0):
    a=[]
    for i in range(0,5):
        b=random.randint(1,6)
        a.append(b)
    a.sort()
    if(a==[1,2,3,4,5] or a==[2,3,4,5,6]):
        c+=1
    # print(a)
    t-=1
print(c/1000)