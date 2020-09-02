# -*- encoding: utf-8 -*-
# @Time   : 2020/9/1 13:18
# @Author : Peter young
# @File   : 91.解码的方法.py

res = 0

s = "226"


dp = [1, 1] + [0] * len(s)
s = "99" + s
print(s)
print(len(s))
for i in range(2, len(s)):
    if s[i] != "0":
        dp[i] += dp[i - 1]
    if 10 <= int(s[i - 1:i + 1]) <= 26:
        dp[i] += dp[i - 2]
print(dp)
print(dp[-1])
