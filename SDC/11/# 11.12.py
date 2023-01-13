# 11.12
import random
a1="abcdefghijklmnopqrstuvwxyz"
a=list(a1)
b=list(a1)
random.shuffle(a)
d={}
for i in range(26):
    d[b[i]]=a[i]
# print(d)
c=str(input())
e=""
for i in range(len(c)):
   e+=d[c[i]] 
print(e)