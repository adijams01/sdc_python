# 13.13
def convert_time():
    a=list(map(int,input().split(":")))
    # print(a[0],a[1])
    c="A"*5+"B"*5+"C"*5+"D"*5+"E"*5
    
    b=(a[0])%5+1
    b1=a[0]+1
    if(a[0]==24):
        b=1
    print(str(b)+c[b]+":"+str(a[1]))    
convert_time()