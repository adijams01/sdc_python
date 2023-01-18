# 14.1
class bank_account():
    def __init__(self,name,amount,interest_rate):
       self.name=name
       self.amount=amount
       self.interest_rate=interest_rate
    
    def interest(self):
        self.new=self.amount*self.interest_rate/100+self.amount
        print(self.name,self.n)
a=str(input())
b=int(input())
c=int(input())
d=int(input())

z=bank_account(a,b,c)
z.interest()
# print(zz)
z=bank_account(a,b,d)
z.interest()

       