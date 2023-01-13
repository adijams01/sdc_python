# 11.9
a={}
t=5
while(t>0):
    b=str(input())
    c=list(map(int,input().split()))
    a[b]=c    
    t-=1
    
d=int(input())
for i in a.keys():
    if(d in a[i]):
        print(i)