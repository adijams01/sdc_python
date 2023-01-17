# 13.10
import random
def rand_lower_string():
    a=int(input())
    s=""
    b="abcdefghijklmnopqrstuvwxyz"
    for i in range(a):
        s+=random.choice(b)
    print(s)
rand_lower_string()