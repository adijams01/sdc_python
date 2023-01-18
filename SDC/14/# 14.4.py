# 14.4
class RestaurantCheck():
    def __init__(self,check_number,sales_tax_percent,subtotal,table_number,server_name):
        self.check_number=check_number
        self.sales_tax_percent=sales_tax_percent
        self.subtotal=subtotal
        self.table_number=table_number
        self.server_name=server_name
    def calculate_total(self):
        self.total=round(self.subtotal+self.subtotal*self.sales_tax_percent/100,2)
        print(self.total)
    def print_check(self):
        file = open("check###", 'w')
        file.write("Check Number: "+str(self.check_number)+"\n")
        file.write("Sales Tax: "+str(self.sales_tax_percent)+"\n")
        file.write("Subtotal: "+str(self.subtotal)+"\n")
        file.write("Total: "+str(self.table_number)+"\n")
        file.write("Server: "+str(self.server_name)+"\n")
check_num=int(input("check : "))
tax=float(input("tax : "))
subtot=float(input("sub : "))
table=int(input("table : "))
name=str(input("name : "))

a=RestaurantCheck(check_num,tax,subtot,table,name)
a.calculate_total()
a.print_check()
