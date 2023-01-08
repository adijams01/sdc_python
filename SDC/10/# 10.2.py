# 10.2
a=str(input())
b=a.split(";")
s=0
for i in range(len(b)):
    s+=int(b[i])
print(s)


