# 7.23
import random
n=int(input())
a=[]
for i in range(0,n):
    a.append(random.randint(90,100))
    
i=random.randint(0,n-1)
a[i]=0
print(a)