# 10.11
a=list(map(str,input().split("/")))
b=[]
b.append(int(a[0]))
b.append(int(a[1]))
print(b)
c=[0,31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(12):
    if(b[0]==i):
        if(b[1]<=c[i]):
            print("correct")
        else:
            print("incorrect")
    
    