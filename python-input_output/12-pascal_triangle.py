#!/usr/bin/python3

def pascal_triangle(n):
    pascal_list = []
    if n > 0:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
            pascal_list.append(row)
            
    return pascal_list