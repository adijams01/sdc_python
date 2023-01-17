# 13.24
import random 
def teams():
    a = ['A','B','C','D','E','F','G','H','I','J']
    n = len(a)
    
    
    
    t=1
    z=1
    while(t==1):
        b = random.choice(a)
        c = random.choice(a)
        if(b!=c):
            print("Team : "+str(z)+" "+ b + ", " + c)
            a.remove(b)
            a.remove(c)
            z+=1
        if(len(a)==0):
            break
teams()