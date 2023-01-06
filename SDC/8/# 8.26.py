# 8.26
import random
a=[0,1,1,1,1,1,1,1,1,1]
a2=[]
for i in range(10):
    b2=[]
    for j in range(10):
        b2.append(random.choice(a))
    a2.append(b2)
for i in range(10):
    print(a2[i])