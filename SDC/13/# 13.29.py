# 13.29
def find_words():
    b=str(input())
    with open(r"C:\Users\HP\Documents\SDC\13\13.29.txt", "r") as file:
        data=file.read()
        a=(data.split("\n"))
    # print(a)
    for i in range(len(a)):
        if(b in a[i]):
            print(a[i])
    
find_words()