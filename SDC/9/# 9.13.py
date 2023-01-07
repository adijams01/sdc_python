# 9.13
# not working properly
# 2 cases i!=len(a)'-1' and '-2'
import random
a=list(map(int,input().split()))
i=0
c=0
while(c!=3 or i!=len(a)-2):
# for i in range(len(a)):
    if(a[i]<0):
        a[i]=0
        c+=1
    if(i!=len(a)-1):
        i+=1
    print(i)
print(a)