# 12.21
import csv
with open(r"C:\Users\HP\Documents\SDC\12\nfl1978-2013.csv", "r") as file:
    # data=file.read()
    a=[line.strip() for line in file]
    
    for i in range(len(a)):
        a[i]=a[i].lower()
    
x=str(input("1 : "))
y=str(input("2 : "))
for line in a[1:]:
    d,t1,s1,t2,s2=line.split(",")
    if((t1==x and t2==y) or (t1==y and t2==x)):
        if(s1=="0" or s2=="0"):
            print(line)
