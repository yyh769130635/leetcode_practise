# -*- encoding: utf-8 -*-
# @Time   : 2020/9/14 21:25
# @Author : Peter young
# @File   : 面试题 17.10. 主要元素.py

class Solution:
    def majorityElement(self, nums):
        dic = {}
        n = len(nums)
        mid = n // 2 + 1
        for i in nums:
            print(dic)
            if i in dic:
                dic[i] += 1
                if dic[i] >= mid:
                    return i
            else:
                dic[i] = 1
                if dic[i] >= mid:
                    return i

        return -1


nums = [1]
print(Solution().majorityElement(nums))