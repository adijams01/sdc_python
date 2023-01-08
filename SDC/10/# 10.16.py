# 10.16
n=9
a=[]
for i in range(1,n+1):
    b=[]
    for j in range(1,n+1):
        b.append("("+str(i)+","+str(j)+")")
    a.append(b)
for i in range(n):
    print(a[i])