# 8.25
import random
a=[]
for i in range(10):
    a.append(0)
for i in range(90):
    a.append(1)
# print(a)
random.shuffle(a)
b1=a
# print(a)
# print(b1)
a2=[]
for i in range(10):
    b=[]
    for j in range(10):
        b.append(random.choice(a))
    a2.append(b)
for i in range(10):
    print(a2[i])
