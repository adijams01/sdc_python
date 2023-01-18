# 14.3
class shoppingcart():
    def __init__(self):
        self.name=[]
        self.amount=[]
    def add(self):
        t="yes"
        while(t=="yes"):
            name=str(input("name : "))
            amount=int(input("amount : "))
            self.name.append(name)
            self.amount.append(amount)
            t=str(input("continue?\n"))
    def total(self):
        print("Total : ",sum(self.amount))
    def cart(self):
        for i in range(len(self.name)):
            print(self.name[i],"\t",self.amount[i])
        print("Total : ",sum(self.amount))
    def remove(self):
        tt="remove?\n"
        if(tt=="yes"):
            num=int(input("num. of elements?\n"))
            for i in range(num):
                p=input("name?\n")
                q=self.name.index(p)
                r=self.name.pop(q)
                k=self.amount.pop(q)
a=shoppingcart()
a.add()
# a.total()
a.remove()
a.cart()