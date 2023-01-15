# 12.10
d=open(r"C:\Users\HP\Documents\SDC\12\12_10_2_new.txt","w")
with open(r"C:\Users\HP\Documents\SDC\12\12_10_2.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
c=[]
for i in range(len(a)):
    # print(a[i])
    b=a[i].split("\\t ")
    # print(b[len(b)-1])
    
    
    # print()
    if(int(b[5])>=20 and float(b[len(b)-1])>=0.3):
        c.append(b[0]+"\n")
d.writelines(c)
print(c)