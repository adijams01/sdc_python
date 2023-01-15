# 12.1
f=r"C:\Users\HP\Documents\SDC\12\expenses.txt"
c=0
with open(f,'r') as file:
    for line in file:
        line=int(line)
        if(line>=2000):
            c+=1
            print(line)
print(c)