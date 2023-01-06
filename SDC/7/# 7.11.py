# 7.11
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if(a[i]%2==0):
        a[i]=0
print(a)
for i in range(0,len(a)):
    if(a[i]%2!=0):
        a[i]=1
print(a)