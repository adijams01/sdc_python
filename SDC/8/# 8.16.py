# 8.16
# not 100% working ,end "."
a=str(input())
b=a.split(".")
for i in range(0,len(b)):
    c=b[i]
    c=c.split()
    
    print(c[-1])