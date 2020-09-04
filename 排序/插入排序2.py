# -*- encoding: utf-8 -*-
# @Time   : 2020/9/2 21:37
# @Author : Peter young
# @File   : 插入排序2.py

def insert_sort(nums):
    # i = 0
    j = 0
    for i in range(2, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[0] = nums[i]
            for j in range(i - 1, 0, -1):
                if nums[j] > nums[0]:
                    nums[j+1] = nums[j]
                else:
                    break
            nums[j+1] = nums[0]
    return nums


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    # d0 = [0, 1, 2, 4, 3]
    d = []
    d1 = insert_sort(d0)
    print(d1)
    print(d0_out)
    # print(d0_out == d1)
