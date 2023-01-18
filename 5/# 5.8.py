# 5.8
import random
c=0
for i in range(10000):
    a=random.randint(1,6)
    b=random.randint(1,6) 
    if(a==b):
        c+=1
print(c/100)
    