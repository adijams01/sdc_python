# 13.14
def next_name():
    a=str(input())
    
    b=[]
    
    for i in range(len(a)):
        b.append((ord(a[i])))
        
    
    b.reverse()
        
    for i in range(len(b)):
        
        if(b[i]+1<=122):
            
            b[i]=b[i]+1
            break
        else:
            b[i]=97
            
    b.reverse()
    # print(b)
    s=""
    for i in range(len(b)):
        s+=chr(b[i])
    print(s)
next_name()