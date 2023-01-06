# 8.20
import random
n=10
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        c=random.randint(0,1)
        b.append(c)
    a.append(b)

for i in range(n):
    print(a[i])

k,l=map(int,(input().split()))

if(a[k][l]==0):
    print("miss")
else:
    print("hit")

        