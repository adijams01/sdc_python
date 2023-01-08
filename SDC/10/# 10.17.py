# 10.17
z=int(input())
n=9
a=[]
for i in range(1,n+1):
    b=[]
    for j in range(1,n+1):
        b.append("("+str(i)+","+str(j)+")")
    a.append(b)
if(z==1):
    for i in range(n):
        for j in range(n):
            if(i>=j):
                print(a[i][j],end=" ")
        print()
else:
    for i in range(n):
        for j in range(n):
            if(i<=j):
                print(a[i][j],end=" ")
        print()
    