# 12.18
import random
with open(r"C:\Users\HP\Documents\SDC\12\12_18.txt", "r") as file:
    data=file.read()
    a=(data.split("\n\n"))
# print(a)
d={}
e=[]
for i in range(len(a)):
    a1=a[i].split(":\n")
    # print(a1)
    b=a1[1].split("\n")
    # print(b)
    e.append(b)
    d[a1[0]]=b

# print(*e[2])
co=["Africa","Asia","Europe","North america","South america","Australia"]
r=random.randint(0,4)
t=(random.choice(e[r]))
print(t)
ff=str(input())
kk=0
for i in range(len(co)):
    if(ff==co[i]):
        kk=i
if(t in e[kk]):
    print("yes")
else:
    print("no")
    for i in range(len(e)):
        if(t in e[i]):
            print(co[i])