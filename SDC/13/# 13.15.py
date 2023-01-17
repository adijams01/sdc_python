# 13.15
def reverse_only_letters():
    a=str(input())
    b=list(a)
    if(len(a)%2==0):
        n=len(a)//2
    else:
        n=(len(a)//2)+1
    print(b)
    for i in range(n):
        if(b[i].isalpha()==True):
            t=b[i]
            b[i]=b[len(b)-1-i]
            b[len(b)-1-i]=t
    print(b)
reverse_only_letters()
            
    