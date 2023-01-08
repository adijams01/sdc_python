# 10.8
import random
z=int(input())
if(z==1):
    t=10
    a=[]
    
    b=[]
    c=[]
    d=[]
    for i in range(32):
        b.append(i)
    for i in range(13):
        d.append(i)
    
    while(t>0):
        
        a.append(random.choice(b))
        a.append(random.choice(d))
        print(a[0],"/",a[1],"/ 2023")
        t-=1
        
else:
    a=[]

    c=""
    for i in range(0,13):
        for j in range(0,32):
            c=str(j)+"/"+str(i)+"/2023"
            # print(c)
            a.append(c)
    # print(a)
    sample = random.sample(a, 10)
    for i in range(10):
        print(sample[i])