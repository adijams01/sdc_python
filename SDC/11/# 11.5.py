# 11.5
a="abcdefghijklmnopqrstuvwxyz"
a+=a.upper()
d={}
print(a)
for i in range(52):
   d[a[i]]=ord(a[i]) 
print(d)
