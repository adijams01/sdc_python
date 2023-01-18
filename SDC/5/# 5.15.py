# 5.15
n=int(input())
a=[1,1]
for i in range(2,n):
    b=a[i-1]*2+a[i-2]
    a.append(b)
print(a)