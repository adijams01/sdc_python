# 28
a=str(input())
for i in range(0,len(a)):
    n=ord(a[i])
    if(a[i]=="a"):
        n+=26
    print(chr(n-1))

    