# -*- encoding: utf-8 -*-
# @Time   : 2020/9/14 21:38
# @Author : Peter young
# @File   : 977. 有序数组的平方.py

# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         i = 0
#         j = len(A)-1
#         res = []
#         while i<=j:
#             if abs(A[i])>abs(A[j]):
#                 res.insert(0,A[i]*A[i])
#                 i+=1
#             else:
#                 res.insert(0,A[j]*A[j])
#                 j-=1
#         return res

