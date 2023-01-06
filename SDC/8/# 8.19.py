# 8.19
import random
n=6
a=[]
for i in range(n):
    row=[]
    for j in range(n):
        b=random.randint(0,9)
        row.append(b)    
    a.append(row)
    
for i in range(n):
    print(a[i])

z=int(input())

if(z==1):
    for i in range(n):
        print(a[i])    
if(z==2):
    c=0
    for i in range(n):
        for j in range(n):
            if(a[i][j]==0):
                c+=1
    print(c)
elif(z==3):
    m=a[0][0]
    for i in range(n):
        m=min(m,a[0][i])
    print(m)
elif(z==4):
    m=a[0][2]
    for i in range(n):
        m=max(m,a[i][2])
    print(m)
elif(z==5):
    s=0
    for i in range(n):
        s+=a[n-1][i]
    print(s)
elif(z==6):
    x=[]
    for i in range(n):
        for j in range(n):
            x.append(a[i][j])
    print(a)
elif(z==7):
    x=[]
    for i in range(n):
        y=[]
        for j in range(n):
            y.append(a[j][i])
        x.append(y)
    print(x)