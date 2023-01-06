# 7.7
import random
a=[]
c=0
for i in range(0,20):
    b=random.randint(0,1000)
    a.append(b)
    
    if(b%2==0):
        c+=1
print(a)
print(c)