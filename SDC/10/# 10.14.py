# 10.14
import math
a=0
while(a!=360):
    b=math.radians(a)
    print(a,round(math.sin(b),4),round(math.cos(b),4))
    
    a+=30