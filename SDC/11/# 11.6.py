# 11.6
a={}
b=str(input())
for i in range(len(b)):
   a[b[i]]=b.count(b[i])
print(a)