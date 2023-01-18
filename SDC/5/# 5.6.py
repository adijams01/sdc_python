# 5.6
import random
c=0
for i in range(10):
    a=random.randint(1,5)
    b=int(input())
    if(b==a):
        print("yes")
        c+=1
    else:
        print("no",a)
print("right :",c)
print("wrong :",10-c)
