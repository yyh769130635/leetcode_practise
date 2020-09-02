# -*- encoding: utf-8 -*-
# @Time   : 2020/9/1 17:18
# @Author : Peter young
# @File   : 945. 使数组唯一的最小增量.py

nums = [3, 2, 1, 2, 1, 7]
nums.sort()
move = 0
for i in range(1, len(nums)):
    if nums[i] <= nums[i - 1]:
        pre = nums[i]
        nums[i] = nums[i - 1] + 1
        move += nums[i] - pre
print(move)