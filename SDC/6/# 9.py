# 9
# a=str(input())
a="adfzdf fcsf"
b=a.replace(" ","*")
i=0
j=0
# a[i]

# while(i<=len(b)):
for i in range(0,len(b)):
    # i=0
    if(i%5==0):
        c=a.replace(a[i],"!",1)

# c=b.replace(a[0],"!")
print(c)
