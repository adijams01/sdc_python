# 13.7
import math
def phi():
    n=int(input())
    c=0
    for i in range(2,n):
        if(math.gcd(i,n)==1):
            c+=1
            # print(i)
            
    print(c) 
    
phi()