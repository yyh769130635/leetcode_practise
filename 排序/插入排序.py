# -*- coding: utf-8 -*-
# @Time : 8/11/2020 7:38 PM
# @Author : Peter yang

## 逐个插入到前面的有序数中

def insert_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d = []
    d1 = insert_sort(d0)
    # print(d1)
    # print(d0_out)
    print(d0_out == d1)
