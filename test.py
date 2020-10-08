# -*- encoding: utf-8 -*-
# @Time   : 2020/9/21 18:24
# @Author : Peter young
# @File   : test.py

class Solution:
    def reOrderArray(self, array):
        # write code here
        if array == []:
            return []
        i = 0
        for j in range(0, len(array)):
            if array[j] & 1:
                temp = array[j]
                for k in range(j - 1, i-1, -1):
                    array[k + 1] = array[k]

                array[i] = temp
                i += 1
            # print(array)
        return array

array = [1, 2, 3, 4, 5, 6, 7]

s = Solution()
print(s.reOrderArray(array))
