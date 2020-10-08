# -*- encoding: utf-8 -*-
# @Time   : 2020/10/7 16:08
# @Author : Peter young
# @File   : 377. 组合总和 Ⅳ.py

# class Solution:
#     def combinationSum4(self, nums, target: int) -> int:
#         dp = [0] * (target + 1)
#         dp[0] = 1
#
#
#         for i in range(1, target + 1):
#             for j in nums:
#                 if i >= j:
#                     dp[i] += dp[i - j]
#         print(dp)
#         return dp[-1]
#
#
# s = Solution()
# s.combinationSum4([1, 2, 3], 4)

ans = ["apple"]
print("apple" in ans)