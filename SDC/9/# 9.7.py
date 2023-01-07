# 9.7
t=1
while(t>0):
    a=str(input())
    if(a==""):
        break
    c=0
    for i in range(len(a)):
        if(a[i]==a[len(a)-1-i]):
            c+=1
    print(c)
    if(c==len(a)):
        print("yes")
    else:
        print("no")
    
        
        
    