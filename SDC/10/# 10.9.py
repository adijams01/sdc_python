# 10.9
import random
c=[]
t=10
d=[]
while(t>0):
    a=random.randint(2,12)
    b=random.randint(2,12)
    c.append(str(a)+"x"+str(b))
    
    d.append(a*b)
    t-=1
c1=0
for i in range(10):
    print(c[i])
    z=int(input())
    if(z==d[i]):
        print("correct")
        c1+=1
    else:
        print("incorrect")
        print(d[i])
print()        
print(c1)    
        