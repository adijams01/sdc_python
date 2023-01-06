# 8.10
import random
a=[]
for i in range(1,21):
    a.append(i)
# print(a)
for i in range(0,3):
    b=random.randint(1,19)
    c=random.randint(b+1,20)
    d=a[b]
    a[b]=a[c]
    a[c]=d
print(a)