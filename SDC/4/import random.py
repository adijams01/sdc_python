import random
t=10
while(t>0):
    
    a=random.randint(20,50)
    b=random.randint(20,50)
    c=random.randint(20,50)
    
    s=a+b+c
    n=int(input())
    
    if(s==n):
        print("Right")
    elif(abs(s-n)==5):
        print("Close")
        
    else:
        print("Wrong")
    
    t-=1