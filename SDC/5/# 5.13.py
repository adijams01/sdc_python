# 5.13
b=[]
for i in range(10):
    a=int(input())
    if(a>=50):
        b.append(a)
        
b.sort()
print(b[0])