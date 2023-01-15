# 12.6
import random
with open(r"C:\Users\HP\Documents\SDC\12\first_names_12_6.txt", "r") as file:
    data=file.read()
    a=(data.split("\n"))
with open(r"C:\Users\HP\Documents\SDC\12\last_names_12_6.txt", "r") as file:
    data1=file.read()
    b=(data1.split("\n"))
for i in range(10):
    print(random.choice(a),random.choice(b))
    