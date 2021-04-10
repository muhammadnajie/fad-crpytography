#!/usr/bin/env python3

def possibility_change(x, y):
    return 2*x*y - x - y

def number_of_cell_value_changes(x, y):
    changes = 0
    for i in range(x):
        for j in range(y-1):
            if matrix[i][j] != matrix[i][j+1]:
                changes += 1

    for j in range(y):
        for i in range(x-1):
            if matrix[j][i] != matrix[j][i+1]:
                changes += 1
    return changes
    
def region_complexity(x, y):
    return number_of_cell_value_changes(x, y) / possibility_change(x,y)

def main():
    global matrix
    matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    x = len(matrix)
    y = len(matrix[0])
    x_complexity = region_complexity(x, y)
    print(x_complexity)

main()