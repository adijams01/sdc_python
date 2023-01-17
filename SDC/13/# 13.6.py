# 13.6
def add_up_range():
    a=int(input())
    b=int(input())
    c=int(input())
    s=0
    for i in range(a,b,c):
        s+=i
    print(s)
add_up_range()