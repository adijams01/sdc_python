# 5.11
import random
f=0
for i in range(20):
    a=random.randint(1,10)
    print(a,end=" ")
    if(a==10):
        f=1
print()
if(f==1):
    print("yes")
else:
    print("no")