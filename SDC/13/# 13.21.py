# 13.21
def telephone_match():
    a=str(input())
    b1=str(input())
    b1=b1.replace("-","")
    b=list(b1)
    print(b)
    c=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
    
    for i in range(len(b)):
        if(a[i] in c[int(b[i])-2]):
            print("yes")
        else:
            print("no")
    # print(c[2])
telephone_match()
    
    
    
    