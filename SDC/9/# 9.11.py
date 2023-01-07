# 9.11
import random
a=[]
b=0
for i in range(50):   
    t=b
    while(t==b):
        b=random.randint(1,5)
    a.append(b)
print(a) 