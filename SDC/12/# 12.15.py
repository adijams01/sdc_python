# 12.15
# nba
with open(r"C:\Users\HP\Documents\SDC\12\12_15_nba.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
# nfl
with open(r"C:\Users\HP\Documents\SDC\12\12_15_nfl.txt", "r") as file:
    data1=file.read()
    a1=(data1.split("\n"))    
c=[]
c1=[]
for i in range(len(a)):
    b=a[i].split(" - The ")
    # print(b)
    c.append(b[1])
for i in range(len(a1)):
    b1=a1[i].split(" - The ")
    # print(b1)
    c1.append(b1[1])
    
for i in c1:
    for j in range(len(i)):
        if(i[:j]+i[j+1:] in c):
            print(i,"and",i[:j]+i[j+1:])
    