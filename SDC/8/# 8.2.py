# 8.2
import random


a=""
b=["H","T"]

for i in range(0,100):
    c=random.choices(b,weights=[1,2])
    a+=str(c)[2:-2]

print(a)