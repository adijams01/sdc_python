# 12.16
# incomplete
with open(r"C:\Users\HP\Documents\SDC\12\12.6.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
print(a)
for i in range(len(a)):
    b1=a[i].split(" ")
b1.sort()
d={}
for i in b1:
    if(i in d.keys()):
        d[i]=d.get(i)+1
    
print(d)