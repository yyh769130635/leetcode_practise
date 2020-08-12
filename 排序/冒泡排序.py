# -*- coding: utf-8 -*-
# @Time : 8/11/2020 3:30 PM
# @Author : Peter yang

# 冒泡排序 【前后比较-交换】

import operator
import copy


d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序

n = len(d0)
while True:
    state = 0
    for i in range(n - 1):
        if d0[i] > d0[i + 1]:
            d0[i], d0[i + 1] = d0[i + 1], d0[i]
            state = 1
    if not state:
        break

print(d0)
d1 = d0
d2 = copy.deepcopy(d0)
print(d0_out)
print(d0 == d0_out)
print(d0 is d0_out)
print(d0 is d1)
print(d0 is d2)
