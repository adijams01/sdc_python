# 8.15
from itertools import permutations
for x in permutations('abcd'):
    a=""
    for i in x:
        a+=i
    print(a,end=", ")
    