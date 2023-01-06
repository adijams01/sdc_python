# 7
a=str(input())
b=a.rfind(".")
c=a.rfind(",")
d=a.rfind(";")
if(b>0 or c>0 or d>0):
    print("There is some punctuation")
else:
    x=a.count(" ")
    print(x)
