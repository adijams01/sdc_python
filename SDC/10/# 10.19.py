# 10.19
a=list(map(int,(input().split())))
b=a
f=0
c=[]
while(f==0):
    for i in range(len(a)):
        for j in range(i+1,len(b)):
            if(a[i]==b[j]):
                c.append(j)
                f=1
                # break
        # break
            
print(c[0])
 