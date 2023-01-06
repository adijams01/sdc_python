# 8.18
z=list(map(int,input().split()))
a=[]
b=[]
c=[]
d=[]
f=[]
for i in range(0,len(z)):
    if(z[i]>=90):
        a.append(z[i])
    elif(z[i]<90 and z[i]>=80):
        b.append(z[i])
    elif(z[i]<80 and z[i]>=70):
        c.append(z[i])
    elif(z[i]<70 and z[i]>=60):
        d.append(z[i])
    else:
        f.append(z[i])
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(f)

print(l)
        