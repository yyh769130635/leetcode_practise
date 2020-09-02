# -*- encoding: utf-8 -*-
# @Time   : 2020/9/2 11:45
# @Author : Peter young
# @File   : 647. 回文子串.py

s = "aaa"
substrings = []
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        if s[i:j] == s[i:j][::-1]:
            substrings.append(s[i:j])

print(substrings)
