# -*- encoding: utf-8 -*-
# @Time   : 2020/9/14 21:11
# @Author : Peter young
# @File   : 面试题 17.21. 直方图的水量.py

class Solution:
    def trap(self, height):
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        print(left)
        print(right)
        res = 0
        for i in range(1, n - 1):
            small = min(left[i], right[i])
            if height[i] < small:
                res += small - height[i]
        print(res)


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
s.trap(height)
