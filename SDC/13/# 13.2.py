# 13.2
def get_bill_total():
    a,b=map(float,(input().split()))
    c=a+a*b/100
    print(round(c,2))
get_bill_total()