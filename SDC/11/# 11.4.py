# 11.4
t=1
a={}
while(t>0):
    v="aeiou"
    b=str(input())
    c=0
    for i in range(len(b)):
        for j in range(len(v)):
            if(b[i]==v[j]):
                c+=1
    a[b]=c
    print(a)