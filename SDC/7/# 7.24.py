# 7.24
import random
a=[]
c=0
for i in range(0,100):
    b=random.randint(1,50)
    if(b==50 and c<2):
        b=-999
        c+=1
    a.append(b)
      
print(a)
if(c==0):
    print("No 50")
