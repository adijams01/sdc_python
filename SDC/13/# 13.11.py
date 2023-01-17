# 13.11
def contains_a_letter():
    a=str(input())
    b=False
    for i in range(len(a)):
        if(a[i].isalpha()==True):
            b=True
    return(b)

c=contains_a_letter()
if(c==True):
    print("yes")
else:
    print("no")