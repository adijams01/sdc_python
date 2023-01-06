# 7.22
a=str(input())
# a.sort()
b=[]
z="abcdefghijklmnopqrstuvwxyz"
for j in range(0,len(z)):
    c=0
    for i in range(0,len(a)):
        if(a[i]==z[j]):
            c+=1
    b.append(c)
    
print(b)