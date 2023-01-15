# 12.17
import random

print("continue?")
g=str(input())
if(g=="yes"):
    with open(r"C:\Users\HP\Documents\SDC\12\12._17.txt", "r") as file:
        data=file.read()
        a1=(data.split("\n"))
    for i in range(len(a1)):
        b1=a1[i].split(" ")
        c=int(b1[0])
        c1=int(b1[1])
else:
    c1=0
    c=0
print("starting points",c,c1)

b=1
z=[]
while(b!=0):
    a=random.randint(1,5)
    b=int(input())
    # b=int(b1)
    if(b==a):
        c+=1
    else:
        c1+=1
    print(a)
z.append(str(c)+" "+str(c1))
print("do you want to save it?")
gg=str(input())
if(gg=="yes"):
    x=open(r"C:\Users\HP\Documents\SDC\12\12._17.txt","w")
    x.writelines(z)
