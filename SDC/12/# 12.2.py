# 12.2
a=open(r"C:\Users\HP\Documents\SDC\12\expenses.txt")
b=open(r"C:\Users\HP\Documents\SDC\12\new_expenses.txt","w")
c=[]
while(1>0):
    s=a.readline()
    if(s==""):
        break
    else:
        s=int(s)
        s=str(round((s+s*0.1),2))
        c.append(s+"\n")
# print(c)
b.writelines(c)
a.close()
