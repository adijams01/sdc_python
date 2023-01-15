# 12.3
with open(r"C:\Users\HP\Documents\SDC\12\12_3.txt", "r") as file:
    data = file.read()
    # print(data)    
    # for line in data:
    # print(data[1:])
    a=(data.split("\n"))
    for i in range(len(a)):
        print(a[i][0])