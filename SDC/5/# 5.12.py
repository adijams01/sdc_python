# 5.12
import random
b=[]
c=0
for i in range(20):
    a=random.randint(1,10)
    # print(a,end=" ")
    b.append(a)
print(b)
for i in range(19):
    c=1
    if(b[i]==b[i+1]):
        c+=1
        print(b[i],"-",c)
        
