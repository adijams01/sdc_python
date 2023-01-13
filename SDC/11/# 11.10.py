# 11.10
import random
a={'2+2':4,'3*3':9,'4/2':2,'2**2':4}
t=1
while(t>0):
    b=random.choice(list(a.keys()))
    print(b)
    c=int(input())
    if(c==a[b]):
        print("yes")
    else:
        print("no")
        break