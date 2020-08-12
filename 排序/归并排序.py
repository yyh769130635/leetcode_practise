# -*- coding: utf-8 -*-
# @Time : 8/11/2020 8:05 PM
# @Author : Peter yang

def merge(a, b):
    c = []
    h = j = 0
    while h < len(a) and j < len(b):
        if a[h] < b[j]:
            c.append(a[h])
            h += 1
        else:
            c.append(b[j])
            j += 1
        if h == len(a):
            # c = c + b[j:]
            c.extend(b[j:])
        if j == len(b):
            # c = c + a[h:]
            c.extend(a[h:])
    return c


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d = []
    d1 = merge_sort(d0)
    print(d1)
    print(d0_out)
    print(d0_out == d1)
