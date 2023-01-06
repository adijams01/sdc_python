# 8.21
import random
n=6
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        c=random.randint(0,2)
        b.append(c)
    a.append(b)
for i in range(n):
    print(a[i])
    
r1,r2,c1,c2=map(int,input().split())
a2=[]
for i in range(r1,r2+1):
    b2=[]
    for j in range(c1,c2+1):
        b2.append(a[i][j])
    a2.append(b2)
s=0
for i in range(len(a2)):
    for j in range(len(a2)):
        s+=a2[i][j]
print(a2)
print(s)
        
