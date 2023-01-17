# 13.18
def closet():
   
    
    
    b=int(input())
    a.sort()
    c=[]
    for i in range(len(a)):
       c.append(abs(a[i]-b) )    
    m=min(c)
    z=c.index(m)
    print(a[z])
closet()