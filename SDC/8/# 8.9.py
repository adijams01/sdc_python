# 8.9
import random
a=str(input())
for i in range(0,len(a)):
    b=random.randint(0,len(a)-1)
    a=a.replace(a[b],"*",1)
    print(a)