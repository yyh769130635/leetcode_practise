# -*- coding: utf-8 -*-
# @Time : 7/28/2020 4:33 PM
# @Author : Peter yang

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution:
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height)-1
        print(left)
        print(right)
        while left < right:
            h = min(height[left], height[right])
            res = max(res, (right - left) * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


obj = Solution()
print(obj.maxArea(height))
