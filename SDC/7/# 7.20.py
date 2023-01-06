# 7.20
import random
a=[]
b=[]
for i in range(0,20):
    a.append(random.randint(0,2))
print(a)
for i in range(0,19):
    if(a[i]==a[i+1]):
        b.append(i+1)
print(b)