# 9.19
n=int(input())
a=[]
while(n>0):
    f=0
    if(n<2):
        f=1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            f=1       
    if(f==0):
        a.append(n)
    n-=1
a.sort()
print(a)
