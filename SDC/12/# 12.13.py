# 12.13
with open(r"C:\Users\HP\Documents\SDC\12\12_13.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
print(a)
b2=[]
for i in range(len(a)):
    b1=list(a[i])
    b1.sort()
    b2.append(b1)
    
b=str(input())
c=list(b)
c.sort()
# print(b2)
# print(c)
for i in range(len(b2)):
    if(b2[i]==c):
        print("yes ",a[i])
        