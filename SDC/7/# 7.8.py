# 7.8
import random
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if(i>=50):
        # print(i)
        b.append(i)
for i in range(0,len(b)):
    c.append(random.choice(b))
print(c)