# -*- coding: utf-8 -*-
# @Time : 8/3/2020 9:56 AM
# @Author : Peter yang
nums = [3,2,1]

l = len(nums)
for i in range(l - 1, -1, -1):
    if nums[i - 1] < nums[i]:  # 找到了需要的 i
        break

if i == 0:  # 代表当前不存在下一个更大的序列，整体翻转即可
    nums[:] = nums[::-1]
    print(nums)

for j in range(l - 1, i - 1, -1):
    if nums[j] > nums[i - 1]:  # 找到了需要的 j
        break

nums[i - 1], nums[j] = nums[j], nums[i - 1]
nums[i:] = nums[i:][::-1]

print(nums)

