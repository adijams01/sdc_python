from math import atan2
from math import degrees
x,y=map(int,input().split())
z=math.degrees(atan2(y,x))
print("{0:.2f}".format(z))

