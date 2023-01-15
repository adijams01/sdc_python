# 12.14
with open(r"C:\Users\HP\Documents\SDC\12\12_14.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
b1=str(input())
b2=b1.split(" ")
b=b2[0]
n=int(b2[1])
f=0
for i in range(len(a)):
    if(a[i]==b):
        print(a[i-n])
        f=1
if(f!=1):
    print("N0")
    