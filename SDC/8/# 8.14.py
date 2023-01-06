# 8.14
a=str(input())
# print(a[1:])
b=a[0].upper()
for i in range(0,(len(a)-1)):
    # b+=str(a.split(a[1:]))
    if(a[i]==" "):
        b+=a[i+1].upper()
    else:
        b+=a[i+1]
print(b)