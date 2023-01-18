# 14.5
class ticket():
    def __init__(self,cost,time,n):
        self.cost=cost
        self.time=time
        self.n=n
    def __str__(self):
        print("ticket("+str(self.cost),str(self.time)+")")
    def is_evening(self):
        g=self.time.split(":")
        if(int(g[0])>=18 and int(g[0])<23):
            print("Evening")
        else:
            print("Not in Evening")
    def bulk_discount(self):
        if(int(self.n)>=5 and int(self.n)<10):
            z=self.cost+self.cost*0.1
            print("10 % dis")
            print("total :",z*self.n)
        elif(int(self.n)>=10):
            z=self.cost+self.cost*0.1
            print("20 % dis")
            print("total :",z*self.n)
        else:
            z=self.cost
            print("no dis")
            print("total :",z*self.n)
            
c=int(input())
t=str(input())
n=int(input())
a=ticket(c,t,n)
a.__str__()
a.is_evening()
a.bulk_discount()