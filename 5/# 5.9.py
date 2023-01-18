# 5.9
import random
c=0
for i in range(10000):
    a=random.randint(1,6)
    b=random.randint(1,6) 
    c=random.randint(1,6)
    d=random.randint(1,6) 
    e=random.randint(1,6) 
    if(a==b==c==d==e):
        c+=1
print(c/100)
    