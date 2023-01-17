# 13.12
def simplify_text():
    a=str(input()).lower()
    b=",.!:;"
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if(a[i]==b[j]):
    a=a.replace(",","")
    a=a.replace(".","")
    a=a.replace("!","")
    a=a.replace(":","")
    a=a.replace(";","")
    print(a)
simplify_text()
        