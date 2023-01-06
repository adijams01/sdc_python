# 8.22
import random
n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        c=random.randint(0,2)
        b.append(c)
    a.append(b)

# for i in range(n):
#     print(a)

a2=[]
for i in range(n):
    b2=[]
    for j in range(i+1):
        b2.append(a[i][j])
    a2.append(b2)

s=0    
for i in range(n):
    for j in range(i+1):
        s+=a2[i][j]
# print(a2)
print(s)
    