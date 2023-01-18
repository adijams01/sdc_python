# 14.11
class calender():
    def __init__(self,year):
        self.year=year
    def is_leap_year(self):
        if(self.year%4==0):
            if(self.year%100!=0 or self.year%400==0):
                return True
                # print("leap year")
            else:
                return False
                # print("not a leap year")
        else:
            return False
            # print("not a leap year")
                
    def firstdayin(self,m):
        p=(14-m)//12
        q=self.year-p
        r=q+q//4-q//100+q//400
        s=m+12*p-2
        t=(1+r+(31*s)//12)%7
        # print(t)
        return t
    def print_calender(self,m):
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        if self.is_leap_year() and m==2:
            days[1]=29
        day_1=self.firstdayin(m)
        print("Sun Mon Tue Wed Thr Fri Sat")
        for i in range(day_1):
            print("    ", end="")
        for day in range(1,days[m-1]+1):
            print(f"{day:2}  ",end="")
            if(day+day_1)%7==0:
                print()
        
y=int(input("enter year : "))
a=calender(y)

if(a.is_leap_year()==True):
    print("is leap year")
else:
    print("not a leap year")
b=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
m=int(input("enter month : "))
print("First day :",b[a.firstdayin(m)])
a.print_calender(1)