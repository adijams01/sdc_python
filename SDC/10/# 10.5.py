# 10.5
a=list(map(str,input().split()))
for i in range(len(a)):
    if(a[i].isalpha()==False):
        a[i]=str(int(a[i])+1)
print(*a)