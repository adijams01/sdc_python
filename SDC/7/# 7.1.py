# 7.1
a=list(map(int,input().split()))
# a=[1,2,3,4,5,6,7,8,9,0]
print(len(a))
print(a[3])
print(a[-3:])
print(a[2:])
c=a.index(0)
a.reverse()
print(a)
a.sort()
print(a[len(a)-1],a[0])
print(sum(a))
if(c>=0):
    print(c)
else:
    print("No zeroes")
print(a)
del(a[0])
print(a)
a[len(a)-2]=9876
print(a)
a.append(-500)
print(a)

