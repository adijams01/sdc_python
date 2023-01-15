# 12.5
b=open(r"C:\Users\HP\Documents\SDC\12\new_wordlist_12_5.txt","w")
with open(r"C:\Users\HP\Documents\SDC\12\12.4.txt", "r") as file:
    data = file.read()
    a=(data.split("\n"))
    
c=[]
for i in range(len(a)):
    if(len(a[i])<=5):
        c.append(a[i]+"\n")
b.writelines(c)
print("done")