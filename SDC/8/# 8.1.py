# 8.1
import random
a=list(map(int,input().split()))
b=random.sample(a,4)
print("1 : ",b)
c=random.choice(a)
print("2 : ",c)
random.shuffle(a)
print("3 : ",a)