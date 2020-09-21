# -*- coding: utf-8 -*-
# @Time : 8/11/2020 7:52 PM
# @Author : Peter yang

def quick_sort(nums):
    global cnt
    if len(nums) <= 1:
        return nums
    # mid = nums[len(nums) // 2]
    mid = len(nums) // 2
    t = nums[mid]
    left = []
    right = []
    # nums.remove(mid)
    for i in nums[:mid] + nums[mid + 1:]:
        if i <= t:
            left.append(i)
        else:
            right.append(i)
        cnt += 1
    return quick_sort(left) + [t] + quick_sort(right)


cnt = 0
d0 = [1, 2, 3, 5, 4]
quick_sort(d0)
print(cnt)

# if __name__ == "__main__":
#     d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
#     d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
#     d = []
#     d1 = quick_sort(d0)
#     # print(d1)
#     # print(d0_out)
#     print(d0_out == d1)
