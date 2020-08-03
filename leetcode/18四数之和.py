# -*- coding: utf-8 -*-
# @Time : 7/29/2020 9:32 AM
# @Author : Peter yang


class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        res = []
        nums.sort()

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            newTarget = target - nums[a]
            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                newTarget2 = newTarget - nums[b]
                c = b + 1
                d = n - 1
                while c < d:
                    if (nums[c] + nums[d]) == newTarget2:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        d -= 1
                        c += 1
                    elif (nums[c] + nums[d]) < newTarget2:
                        c += 1
                    else:
                        d -= 1
        return res
