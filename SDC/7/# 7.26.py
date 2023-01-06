# 7.26
import random
a=list(map(int,input().split()))
for i in range(0,len(a)):
    j=random.randint(i,len(a))
    b=a[i]
    a[i]=a[j]
    a[j]=b
print(a)