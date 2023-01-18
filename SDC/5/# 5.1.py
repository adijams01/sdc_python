# 5.1
import random
c=0
for i in range(50):
    a=(random.randint(1,9))
    print(a,end=" ")
    if a==5:
        c+=1
print()
print(c)