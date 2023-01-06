# 8.17
z=int(input())
if(z==1):
    a=[]
    for i in range(1,101):
        a.append(round(i**0.5,2))
    print(a)
elif(z==2):
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        a[i]+=1
    print(a)
elif(z==3):
    a=list(map(int,input().split()))
    b=[]
    for i in range(0,len(a)):
        if(a[i]%2==0):
            b.append(a[i])
    print(b)    
elif(z==4):
    a=list(map(int,input().split()))
    b=[]
    for i in range(0,len(a)):
        b.append(max(a[i],0))
    print(b)    
elif(z==5):
    a=str(input())
    b=[]
    for i in range(0,len(a)):
        if(a[i].isalpha()==True):
            b.append(a[i])
    print(b)    
elif(z==6):
    n=3
    a=[]
    for i in range(n):
        
        b=list(map(int,(input().split())))
        a.append(b[len(b)-1])
    print(a)  
elif(z==7):
    a=str(input())
    b="abcdefghijklmnopqrstuvwxyz"
    d=[]
    for i in range(0,len(b)):
        c=0
        for j in range(0,len(a)):
            if(b[i]==a[j]):
                c+=1
        d.append(c)
    print(d)
elif(z==8):
    a=str(input())
    b=str(input())
    c=[]
    for i in range(0,len(a)):
        
        if(a[i]!=b[i]):
            c.append(i)
    print(c)
                
        
        
        