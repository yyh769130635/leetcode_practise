# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 17:07
# @Author : Peter young
# @File   : 57.py
target = 9
res = []
left = 1
r = 1
s = 0
while r <= (target + 1) // 2:
    s += r
    while s > target:
        s -= left
        left += 1
    if s == target:
        res.append([i for i in range(left, r + 1)])
        r += 1

    else:
        r += 1

print(res)
