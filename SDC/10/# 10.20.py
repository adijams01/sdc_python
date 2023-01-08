# 10.20
# incomplete
import random
n=6
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(random.randint(0,3))
    a.append(b)
for i in range(n):
    print(a[i])
    
x=int(input())
y=int(input())