# 17
a=str(input())
b=str(input())
n=max(len(a),len(b))
m=min(len(a),len(b))
c=0
print(n,m)
for i in range(0,n):
    for j in range(0,m):
        try:
            if(a[i]==b[j]):
                c+=1
        except:
            if(a[j]==b[i]):
                c+=1
            
print(n-c,"characters are diff.")