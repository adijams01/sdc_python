# 14.2
class item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __str__(self):
        print(self.name,round(self.price,2))
    
a=str(input())
b=float(input())
z=item(a,b)
z.__str__()