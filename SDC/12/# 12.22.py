# 12.22
with open(r"C:\Users\HP\Documents\SDC\12\nfl_scores.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
# print(a[1])
b=[]
for i in range(1,len(a)):
    b1=a[i].split(",")
    b2=b1[1].split("-")
    b.append(b2)
    # print(b2)
print(b[5])
print(b[6])
print(b[7])
z1=[]
for i in range(2,30):
# if range is 2-30 change j's 0 to 2
    for j in range(0,i+1):
        z=[]
        
        z.append(str(i))
        z.append(str(j))
        z1.append(z)
c=[x for x in z1 if x not in b]

for i in range(len(c)):
    print(str(c[i][0])+"-"+str(c[i][1]),end=" ,")