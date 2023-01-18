# 5.5
s=0
c=0
for i in range(10):
    a=int(input())
    if(a<0):
        c+=1
    s+=a
print("sum :",s)
print(c)