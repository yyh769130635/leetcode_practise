# -*- encoding: utf-8 -*-
# @Time   : 2020/9/1 14:21
# @Author : Peter young
# @File   : 820. 单词的压缩编码.py

words = ["time", "me", "bell"]
good = set(words)
for word in words:
    for k in range(1, len(word)):
        good.discard(word[k:])

print(sum(len(word) + 1 for word in good))