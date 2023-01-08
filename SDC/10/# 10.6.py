# 10.6
import random
a=[]
for i in range(100,121):
    a.append(i)
# print(a)
d=[]
for i in range(len(a)):
    b=str(a[i])
    c=list(b)
    print(c)
    random.shuffle(c)
    e="".join(c) 
    d.append(e)
for i in range(len(a)):
    
    print(a[i],d[i])