# 13.26
def print_2d():
    rows,cols=2,2
    matrix=[[0 for j in range(cols)] for i in range(rows)]
 
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input("Enter element at position ({},{}): ".format(i, j)))

    print(matrix)
print_2d()