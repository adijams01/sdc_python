# 12.20
#what to do?
with open(r"C:\Users\HP\Documents\SDC\12\12.20.txt", "r") as file:
    data=file.read()
    a=(data.split("\n\n"))
c=[]    
for i in range(len(a)):
    b=a[i].split("\n")
for i in range(len(b)):
    c.append(b[i])
e=[]
for i in range(len(c)):
    d=str(c[i]).split(" ")    
    e.append(int(d[1]))
m=0
for i in range(len(e)-1) :
    if(m>=e[i]-e[i+1]):
        m=e[i]-e[i+1]
        f=i
print(c[f],c[f+1],"have max. increase in 30 day period")