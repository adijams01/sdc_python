# 5.7
import random
c=0
c1=0
c2=0
for i in range(10):
    a=random.randint(1,5)
    b=int(input())
    if(b==a):
        print("yes")
        c+=1
    elif(b==abs(a-2)):
        print("close",a)
        c1+=1
    else:
        print("no",a)
        c2+=1
print("right :",c)
print("close :",c1)
print("wrong :",10-c)
print("Total :",c*5+c1*2-c2)

