# -*- encoding: utf-8 -*-
# @Time   : 2020/9/27 13:19
# @Author : Peter young
# @File   : 剑指 Offer 29. 顺时针打印矩阵.py

def spiralOrder(matrix):
    if matrix == []:
        return []
    res = []
    l = 0
    r = len(matrix[0]) - 1
    up = 0
    down = len(matrix) - 1
    while l <= r and up <= down:
        for i in range(l, r + 1):
            res.append(matrix[up][i])
        for i in range(up + 1, down + 1):
            res.append(matrix[i][r])
        if l < r and up < down:
            for i in range(r - 1, l-1, -1):
                res.append(matrix[down][i])
            for i in range(down-1, up, -1):
                res.append(matrix[i][l])
        l, r, up, down = l + 1, r - 1, up + 1, down - 1
    return res


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix))
