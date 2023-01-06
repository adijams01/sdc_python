# 7.12
a=list(map(int,input().split()))
print(sum(a)/len(a))
a.sort()
print(a[:3])
b=a[1:]
print(sum(b)/len(b))
