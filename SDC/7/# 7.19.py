# 7.19
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    b=a[i]
    a[i]=a[i+1]
    a[i+1]=b
print(a)