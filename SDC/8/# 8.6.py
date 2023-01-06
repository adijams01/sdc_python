# 8.6
import random
v=["look","stay","point","work","wear","rule","stand","find","play","bake"]
n1=["lion","watermelon","table","bicycle","mushroom","shoes","car","noodles","carrot","animal"]
n2=["abroad","alcohol","bathroom","bear","bedroom","bell","bad","bend","benefit","baby"]
a=["abrupt","acidic","curved","brave","dashing","cumbersome","embarrassed","juicy","naughty","nutty"]

vi=random.randint(0,len(v)-1)
n1i=random.randint(0,len(n1)-1)
n2i=random.randint(0,len(n2)-1)
ai=random.randint(0,len(a)-1)

print("The",a[ai],n1[n1i],v[vi],n2[n2i])
    