# -*- coding: utf-8 -*-
# @Time : 8/3/2020 1:07 PM
# @Author : Peter yang

nums = [4, 5, 6, 7, 0, 1, 2]
target = 5

l = 0
r = len(nums) - 1

while l < r:
    mid = (l+r)//2
    if nums[mid]== target:
        print(mid)
    if nums[0]<=nums[mid]:  #左边是有序数组
        if nums[0]<=target<nums[mid]:
            r=mid-1
        else:
            l = mid+1
    else: #右边是有序数组
        if nums[mid]<target<=nums[len(nums)-1]:
            l = mid+1
        else:
            r = mid-1
# print()
