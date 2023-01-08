# 10.3
a=list(map(str,(input().split(","))))
print(a)
b=""
for i in range(len(a)):
    b+=a[i]
c=float(b)
# print(c)
print(c**0.5)
    