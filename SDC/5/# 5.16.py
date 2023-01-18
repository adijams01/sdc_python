# 5.16
a=[1,2,3]
n=int(input())

for i in range(2,n+1):
    b=(a[i]+a[i-1]+a[i-2])/3
    a.append(round(b,3))
print(*a)
    
