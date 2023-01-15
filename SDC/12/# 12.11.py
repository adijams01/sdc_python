# 12.11
d=open(r"C:\Users\HP\Documents\SDC\12\12_11_new.txt","w")
with open(r"C:\Users\HP\Documents\SDC\12\12_11.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
c=[]

m={"01":"january","02":"febuary","03":"march","04":"april","05":"may","06":"june","07":"july","08":"august","09":"september","10":"october","11":"november","12":"december"}
for i in range(len(a)):
    b=a[i].split(" ",2)
    b1=b[0].split("/")
    # b2.append(b1[0],m[b1[1]],b1[2])
    f=int(b[1])
    cel=((f-32)*5)/9
    # print(b1[0],m[b1[1]],b1[2],round(cel,2),b[2])
    c.append(b1[0]+" "+m[b1[1]]+" "+b1[2]+" "+str(round(cel,2))+" "+b[2]+"\n")
d.writelines(c)
# print(c)


    