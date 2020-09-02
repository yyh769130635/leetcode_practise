# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 15:23
# @Author : Peter young
# @File   : 1103. 分糖果 II.py

candies = 7
num_people = 4

res = [0 for _ in range(num_people)]
record = 1
while candies > 0:
    for i in range(num_people):
        if candies - record >= 0:
            res[i] += record
            candies -= record
            record += 1
        else:
            res[i] += candies
            candies = 0
            break
print(res)
