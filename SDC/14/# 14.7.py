# 14.7
class course():
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        self.student_IDS=[]
    def students(self):
        t=self.capacity
        while(t>0):
            Id=str(input("Enter ID : "))
            self.student_IDS.append(Id)
            t-=1
            print("seats left :",t)
    def is_full(self):
        if(self.capacity==len(self.student_IDS)):
            print("seats full")
    def add_student(self):
            Id=str(input("Enter ID to add : "))
            if(Id not in self.student_IDS):
                self.student_IDS.append(Id)
            else:
                print("already in")
            print(self.student_IDS)
n=str(input("name : "))
c=int(input("capacity : "))
a=course(n,c)
a.students()
a.is_full()
a.add_student()
        