# 12.12
with open(r"C:\Users\HP\Documents\SDC\12\12.12.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
# print(a)
b="abcdefghijklmnopqrstuvwxyz"
c=[]
for i in range(len(b)):
    row=[b[i]+" :"]
    for j in range(len(a)):
        if(a[j][0]==b[i]):
            row.append(a[j]+",")
    c.append(row)
for i in range(len(c)):
    print(*c[i])