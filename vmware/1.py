# -*- encoding: utf-8 -*-
# @Time   : 2020/9/21 21:07
# @Author : Peter young
# @File   : 1.py

# n, m, r = 3, 5, 5

n = 7495417.6435616808
m = 10
r = 6125201.7312234128
dis = 0
length = n * 4
for _ in range(m):
    dis = dis + r
    dis = dis % length
    if 0 <= dis <= n:
        j = float(0.0)
        i = round(dis, 2)
        print(i, j)
    elif n < dis <= n * 2:
        i = float(n)
        j = float(dis - n)
        print(i, j)
    elif n * 2 < dis <= n * 3:
        j = float(n)
        i = float(3 * n - dis)
        print(i, j)
    else:
        j = float(4 * n - dis)
        i = float(0)
        print(i, j)
