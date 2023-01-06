y,m,d=map(int,input().split())
p=(14-m)//12
q=y-p
r=q+(q//4)-(q//100)+(q//400)
s=m+12*p-2
t=((d+r+((31*s)//12))*10)%7
a=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(a[t])