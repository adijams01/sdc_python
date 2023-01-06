# 8.23
import random
n=6
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        c=random.randint(0,5)
        b.append(c)
    a.append(b)
for i in range(n):
    print(a[i])
c1=0
for i in range(n):
    for j in range(n-1):
        if(a[i][j]==a[i][j+1] and a[i][j]==0):
            c1+=1
print("in a row :",c1)

c2=0
for i in range(n):
    for j in range(n-1):
        if(a[j][i]==a[j+1][i] and a[j][i]==0):
            c2+=1
print("in a column :",c2)

    
