# 7.10
a=list(map(int,input().split()))
a.sort
m=a[len(a)-1]
for i in range(0,len(a)):
    if(a[i]>10):
        if(a[i]<m):
            m=a[i]
print(m)