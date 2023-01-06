# 8.3.
import random


a=""
b=["A","B","C","D"]

for i in range(0,100):
    c=random.choices(b,weights=[6,3,0.8,0.2])
    a+=str(c)[2:-2]

print(a)