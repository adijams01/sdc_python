# 11.11
a=[0 for i in range(10)]
b=list(input().split()) 
c=list(input().split()) 
for i in range(len(b)):
    a[int(b[i])]=c[i]
d=int(input())    
print(a[d])