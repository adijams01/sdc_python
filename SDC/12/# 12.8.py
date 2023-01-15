# 12.8
with open(r"C:\Users\HP\Documents\SDC\12\12_8.txt", "r") as file:
    data=file.read()
    a=(data.split("\n\n"))
for i in range(len(a)):
    # print(a[i])
    b=a[i].split(":\n")
    
    if(len(b[1])>=200):
        print(b[0],"A")
    elif(len(b[1])>=150 and len(b[1])<200):
        print(b[0],"B")
    elif(len(b[1])>=100 and len(b[1])<150):
        print(b[0],"C")
    elif(len(b[1])>=50 and len(b[1])<100):
        print(b[0],"D")
    else:
        print(b[0],"F")
        
        
    
        