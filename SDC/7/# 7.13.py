# 7.13
x=int(input())
i=int(input())
if(x==1):
    
    if(i==1):
        print("january")
    elif(i==2):
        print("feburary")
    elif(i==3):
        print("march")
    elif(i==4):
        print("april")
    elif(i==5):
        print("may")
    elif(i==6):
        print("june")
    elif(i==7):
        print("july")
    elif(i==8):
        print("august")
    elif(i==9):
        print("september")
    elif(i==10):
        print("october")
    elif(i==11):
        print("november")
    elif(i==12):
        print("december")
        
else:
    
    a=["january","feburary","march","april","may","june","july","august","september","october","november","december"]
    print(a[i-1])