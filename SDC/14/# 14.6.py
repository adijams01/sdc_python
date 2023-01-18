# 14.6
class  movie_name():
    def __init__(self,name,cost,time):
        self.name=name
        self.cost=cost
        self.time=time
    def __str__(self):
        print(self.name,self.cost,self.time)
    def afternoon_discount(self):
        g=self.time.split(":")
        if(int(g[0])>=12 and int(g[0])<18):
            z=self.cost+self.cost*0.1
            print("discounted price :",z)
        else:
            print("no discount")
n=str(input())
c=int(input())
t=str(input())
a=movie_name(n,c,t)
a.__str__()
a.afternoon_discount()