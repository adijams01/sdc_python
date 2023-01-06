# 15
a=str(input())
l=0
u=0
for i in a:
    if(i.islower()):
        l+=1
    elif(i.isupper()):
        u+=1
if(l>u):
    print("l>u")
elif(l<u):
    print("l<u")
else:
    print("l=u")
    
print(l,u)