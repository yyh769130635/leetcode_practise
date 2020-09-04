# -*- encoding: utf-8 -*-
# @Time   : 2020/9/2 14:01
# @Author : Peter young
# @File   : 560. 和为K的子数组.py

nums = [1, 1, 1]
k = 2
dic = {}
dic[0] = 1
s = 0
cnt = 0
for i in nums:
    s += i
    if s - k in dic:
        cnt += dic[s - k]
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
print(cnt)
