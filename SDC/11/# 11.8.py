# 11.8
a={"january":31,"febuary":29,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
b=list(map(str,input().split()))
if(int(b[1])<=a[b[0]]):
    print("yes")
else:
    print("no")