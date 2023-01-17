# 13.25
def triple_shuffle():
    z=3
    while(z>0):
       
       
        a=list(map(int,input().split()))
        a.reverse()
        t=a[0]
        a[0]=a[1]
        a[1]=t
        print(a)
        z-=1
triple_shuffle()