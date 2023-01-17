# 13.28
def number_of_lines():
    with open(r"C:\Users\HP\Documents\SDC\13\13_28.txt", "r") as file:
        data=file.read()
        a=(data.split("\n"))
    print(len(a))
number_of_lines()