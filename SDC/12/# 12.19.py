# 12.19
import random
d=open(r"C:\Users\HP\Documents\SDC\12\12.19_new.txt","w")
with open(r"C:\Users\HP\Documents\SDC\12\12.19.txt", "r") as file:
    data=file.read()
    a=(data.split("\n\n"))
c=[]    
for i in range(len(a)):
    # print(a[i])
    b=a[i].split("\n")
    
    
    # print(b)
    t=b[1]
    b[1]=b[2]
    b[2]=t
    # print(str(b))
    for i in range(len(b)):
        
        c.append((b[i])+"\n")
# print(c)
d.writelines(c)
