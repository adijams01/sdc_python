# 7.27
a=list(map(str,input().split()))
b=list(map(int,input().split()))
for i in b:
    a.pop(i)
print(a)
