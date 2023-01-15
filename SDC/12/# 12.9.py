# 12.9
d=open(r"C:\Users\HP\Documents\SDC\12\12_9_new.txt","w")
with open(r"C:\Users\HP\Documents\SDC\12\12_9.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
# print(a)
c=[]
for i in range(len(a)):
    b=a[i].split(" ")
    # print(b[1])
    c.append(b[1]+"\n")
d.writelines(c)