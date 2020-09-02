# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 11:28
# @Author : Peter young
# @File   : 89.格雷编码.py
# 关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);

res = []
for i in range(2 ** n):
    res.append(i ^ i >> 1)
print(res)
