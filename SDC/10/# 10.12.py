# 10.12
a=list(map(str,(input().split("d"))))
b=a[1].split("'")
print(round(int(a[0])+int(b[0])/60+int(b[1])/3600,2))