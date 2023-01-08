# 10.10
import random
x=int(input())
if(x==1):
    b=[]
    t=20
    e=[]
    while(t>0):
        a=10
        c=10
        while(a==10 or c==10):
            a=random.randint(2,12)
            c=random.randint(2,12)
        b.append(str(a)+"x"+str(c))
        
        e.append(a*c)
        t-=1
    print(b)
    
else:
    a=[1,2,3,4,5,6,7,8,9,11,12]
    b=[]
    e=[]
    for i in range(11):
        c=random.choice(a)
        d=random.choice(a)
        b.append(str(c)+"x"+str(d))
        e.append(c*d)
        
c1=0
for i in range(20):
    print(b[i])
    z=int(input())
    if(z==e[i]):
        print("correct")
        c1+=1
    else:
        print("incorrect")
        print(e[i])
print()        
print(c1)    