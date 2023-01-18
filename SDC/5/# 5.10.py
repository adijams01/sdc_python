# 5.10
a=list(map(int,(input().split())))
b=min(a[1],a[2])
c=min(a[2],a[3])
i=a.index(b)
j=a.index(c)
t=a[i]
a[i]=a[j]
a[j]=t
print(a)


