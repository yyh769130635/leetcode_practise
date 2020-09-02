# # -*- coding: utf-8 -*-
# # @Time : 8/12/2020 10:27 AM
# # @Author : Peter yang
from collections import Counter

nums = [2, 2, 1, 1, 1, 3]
temp = Counter(nums)
# 按value排序
a = sorted(temp, key=lambda x: temp[x], reverse=True)[:2]
print(a)
