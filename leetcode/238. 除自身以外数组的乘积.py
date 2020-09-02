# -*- encoding: utf-8 -*-
# @Time   : 2020/9/1 16:21
# @Author : Peter young
# @File   : 238. 除自身以外数组的乘积.py

nums = [1, 2, 3, 4]
n = len(nums)
left = 1
right = 1
res = [1]*n
for i in range(len(nums)):
    # print(left)
    res[i] *= left
    left *= nums[i]
    print(right)
    res[n-1-i] *= right
    right *= nums[n-1-i]
print(res)