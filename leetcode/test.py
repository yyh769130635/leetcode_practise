# -*- coding: utf-8 -*-
# @Time : 8/12/2020 10:27 AM
# @Author : Peter yang

s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]

n = len(s)
# if n <= 1:
#     return s in wordDict

i = j = 0
while j < n:
    temp = s[i:j+1]
    if s[i:j + 1] in wordDict:
        j += 1
        i = j
    else:
        j += 1
if i == n:
    print("True")
else:
    print("False")
