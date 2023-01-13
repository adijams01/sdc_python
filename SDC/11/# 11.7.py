# 11.7
d1={}
d2={}
a=str(input())
b=str(input())
for i in range(len(a)):
   d1[a[i]]=a.count(a[i]) 
for i in range(len(b)):
   d2[a[i]]=b.count(b[i]) 
if(d1==d2):
    print("yes")
else:
    print("no")