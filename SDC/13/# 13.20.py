# 13.20
def string_sort():
    a=str(input())
    b=list(a)
    b.sort()
    s=""
    for i in range(len(b)):
        s+=b[i]
    print(s)
string_sort()

