# 10.15
# incomplete
name=['Alice','Bob','Caroline']
birthdays=['2/7/86','11/12/66','8/17/72']
# salaries=[72000,144300,43200]
s=[72000,144300,43200]
salaries=[]
for i in range(3):
    s1=""
    for j in range(len(str(s[i]))):
        s1+=str((s[i])%(j+1))
        salaries.append(s1)
print(salaries)
# a=[]
# # for i in range(3):
# t=3
# while(t>0):
    
#     b=[]
#     # for j in range(3):
#     b.append(name[t-1])
#     b.append(birthdays[t-1])
#     b.append(salaries[t-1])
        
#     a.append(b)
#     t-=1
# d=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         print(a[i][j],end=" ")
#     print()
#     c=(a[i][1].split("/"))
#     d.append(c)
    
# # for i in range(len(a)):
# # print(d)
# for i in range(len(d)):
#     z="0"
#     if(int(d[i][0])<=10):
#         z+=d[i][0]
#         d[i][0]=z
#     z1="0"
#     if(int(d[i][1])<=10):
#         z1+=d[i][1]
#         d[i][1]=z1
#         # print(z)
# # print(*d)
# e=[]
# e.append("/".join(d[0]))
# e.append("/".join(d[1]))
# e.append("/".join(d[2]))
# print(e)
    
# for i in range(3):
#     a[i][1]=e[i]
# print(a)


    