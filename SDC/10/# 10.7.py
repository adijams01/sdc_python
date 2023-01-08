# 10.7
import random
t=int(input())-4
a=[]
b1="abcdefghijklmnopqrstuvwxyz"
b=list(b1)
c1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=list(c1)
d1="0123456789"
d=list(d1)
e=["!","@","#","$","%","^","&","*","(",")"]
a.append(random.choice(b))
a.append(random.choice(c))
a.append(random.choice(d))
while(t>0):
    
    a.append(random.choice(b))
    
    t-=1
a.append(random.choice(e))
a1="".join(a)
print(a1)