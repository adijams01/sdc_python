# 13.17
def mid_range():
     a=list(map(int,input().split()))
     a.sort()
     b=a[0]
     c=a[len(a)-1]
     print((b+c)/2)
mid_range()