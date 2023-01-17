# 13.27
import random
def random_2d_list():
    m=int(input())
    n=int(input())
    x=int(input())
    y=int(input())
    a=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(random.randint(x,y))
        a.append(row)
    print(a)
random_2d_list()
