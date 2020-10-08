# -*- encoding: utf-8 -*-
# @Time   : 2020/10/7 19:53
# @Author : Peter young
# @File   : 1248. 统计「优美子数组」.py

class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        ans = 0
        l = 0
        r = 0
        cnt = 0
        while r < len(nums):
            if nums[r] % 2 == 1:
                cnt += 1
            if cnt == k:
                while nums[l] % 2 == 0:
                    ans += 1
                    l += 1

            r += 1
        return cnt


s = Solution()
print(s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
