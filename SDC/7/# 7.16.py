# 7.16
a=list(map(int,input().split()))
b=[]
c=0
for i in range(0,len(a)):
    c+=a[i]
    b.append(c)
print(b)