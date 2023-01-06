# 8.4
import random

a=0
b=[]
n=int(input())
n1=n
while(n>0):
    for j in range(33,127):
        # a=random.random(j)
        a=chr(j)
        b.append(a)
    n-=1

x=random.sample(b,n1)
x1=""
for i in range(0,n1):
    
    x1+=str((x[i]))
print(x1)