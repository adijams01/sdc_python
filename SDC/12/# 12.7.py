# 12.7
with open(r"C:\Users\HP\Documents\SDC\12\12_7.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
# print(a)
# -1 due to newline character in file ig
for i in range(len(a)-1):
    if(a[i][0]=="g"):
        b=a[i].split(" ")
        if(int(b[1])>=500):
            print(*b)