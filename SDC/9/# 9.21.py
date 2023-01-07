# 9.21
import random
# 0=girl,1=boy
n=10
c=0
b=0
g=0
while(n>0):
    t=0
    c1=0
    while(t==0):
        t=random.randint(0,1)
        # print(t)
        c1+=1
    # print(c)
    c+=c1
    g+=c1-1
    # print("g",g)
    b+=1
    n-=1
print(round((g/c)*100,2),"%")