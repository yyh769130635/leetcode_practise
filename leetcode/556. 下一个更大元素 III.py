# -*- encoding: utf-8 -*-
# @Time   : 2020/9/5 18:47
# @Author : Peter young
# @File   : 556. 下一个更大元素 III.py

n = 1999999999
nums = [int(x) for x in str(n)]
# if len(nums) <= 1:
#     return -1
for i in range(len(nums) - 1, -1, -1):
    if nums[i - 1] < nums[i]:
        break
# if i == 0:
#     return -1

for j in range(len(nums) - 1, i - 1, -1):
    if nums[i - 1] < nums[j]:
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        break
s = nums[:i] + nums[i:][::-1]
res = "".join(map(str,s))
print(res)