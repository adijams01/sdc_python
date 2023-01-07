# 9.14
# can do better
a=str(input())
t=len(a)
# b=[]
b=""
while(t>0):
    if(a[t-1].isalpha()==True):
        # b.append()
        b+=a[t-1]
    else:
        break    
    
    
    t-=1
# b.reverse()
print(b[::-1])