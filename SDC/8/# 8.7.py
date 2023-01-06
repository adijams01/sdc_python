# 8.7
import random
a=["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
b=["clubs","diamonds","hearts","spades"]
c=[]
for i in range(0,4):
    for j in range(0,13):
        d=b[i]+"of"+a[i]
        c.append(d)
# print(c)
random.shuffle(c)
print(c[:5])
        
