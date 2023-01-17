# 13.19
def changes_by_one():
     a=list(map(int,input().split()))
     b=[]
     for i in range(len(a)-1):
         if(a[i]==a[i+1]-1):
             b.append(i+1)
             
             
             
     print(b)
changes_by_one()