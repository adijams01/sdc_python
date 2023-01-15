# 12.4
with open(r"C:\Users\HP\Documents\SDC\12\12.4.txt", "r") as file:
    data = file.read()
    a=(data.split("\n"))
# print(a)
b=0
c=0

zz=[]
for i in range(len(a)):
    
    if("quot" in a[i]):
        print("contains quot",a[i])
      
    if(('a' in a[i] or 'e' in a[i] or 'i' in a[i] or 'o' in a[i] or 'u' in a[i]) and 'y' not in a[i] ):
        c+=1
      
    if(len(a[i])>=6 and a[i][0]==a[i][len(a[i])-1]):
            print("same start and ending letter",a[i])
            zz.append(a[i])
      
    b+=len(a[i])

    for j in range(len(a[i])-3):
        if(a[i][j+1]==chr(ord(a[i][j])+1)) and (a[i][j+2]==chr(ord(a[i][j])+2)) and (a[i][j+3]==chr(ord(a[i][j])+3)):
            # print("alphabetically consecutive",a[i])
            f=a[i]
    # print(i+1)     
    

print(c/len(a)*100)     
print(b//len(a))     
print("no. of same start and end",len(zz))     
zz.sort()
print("longest same start and end",zz[len(zz)-1])
print("alphabetically consecutive",f)     

