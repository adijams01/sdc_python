# 8.24
n=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        if(i==0 or i==n-1 or i==j or j==0 or j==n-1 or i==n-j-1):
            b.append("#")
        else:
            b.append(" ")
            
    a.append(b)

for i in range(n):
    print(*a[i])