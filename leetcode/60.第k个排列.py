# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 10:57
# @Author : Peter young
# @File   : 60.第k个排列.py

n = 3
k = 3
fac = [0 for _ in range(n)]
k = k - 1
fac[n - 1] = 0
for i in range(1, n):
    fac[n - i - 1] = k % (i + 1)
    k //= i + 1
# print(fac)
nums = [i for i in range(1, n + 1)]
res = ""
for i in range(n):
    res += str(nums[fac[i]])
    del nums[fac[i]]
print(res)
