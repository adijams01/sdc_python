# 9.12  
# ezier without while loop???
import random
a=list(map(int,input().split()))
# while(c==1):
for i in range(len(a)):
    if(a[i]<0):
        a[i]=0
        break
print(a)