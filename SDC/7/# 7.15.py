# 7.15
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
    d=max(a[i],b[i])
    c.append(d)
    
print(c)
    