# 7.21
a=list(map(int,input().split()))
for i in range(0,5):
    b=a[:5]
# print(b)
b.reverse()
for i in range(5,len(a)):
    b.append(a[i])
print(b)