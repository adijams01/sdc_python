# 9.23
import random
t=100
a=[]    
while(t>0):
    a.append(t)
    t-=1
a.sort()
# print(a)
c=0
while(len(a)!=0):
    n=20
    b=[0]
    while(n>0):
        d=(random.randint(1,100))
        for i in range(len(b)):
            if(b[i]==d):
                d=(random.randint(1,100))
        b.append(d)
          
        n-=1

    b.sort()
    # print(b)
    for i in range(len(b)):
        try:
            a.remove(b[i])
        except:
            pass
    # print(a)
    c+=1
print(c)