# 9.18
# incomplete
import random
# a=str(input())
a="ad1ty00ki"
t=0
b=[]
while(t!=len(a)-1):
    if(a[t].isalpha()==False):
        b.append(t)
    
    t+=1
for i in range(len(b)):
    
    c=random.choice(b)
    a=a.replace(a[c-i],"")
    # a+=a[:(c-i)]
    # a+=a[(c-i):]
    print(a)
print(b)
print(a)
# print(a[:2])
# print(a[3:])