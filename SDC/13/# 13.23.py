# 13.23
def union():
    
    
    
    
    b=list(map(int,input().split()))
    diff1=[x for x in a if x not in b]
    diff2=[x for x in b if x not in a]
    same=[x for x in a if x in b]
    z=same+diff1+diff2
    print(z)
union()


    