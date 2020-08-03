# -*- coding: utf-8 -*-
# @Time : 8/3/2020 9:09 AM
# @Author : Peter yang

from collections import Counter

words = ["foo", "bar"]
s = "barfoothefoobarman"
# print(Counter(words))

from collections import Counter

# if not s or not words:
#     return []
one_word = len(words[0])
all_words = len(words) * one_word
n = len(s)
res = []
words = Counter(words)

for i in range(0, n - all_words + 1):
    temp1 = s[i:i + all_words]
    temp2 = []
    for j in range(0, all_words, one_word):
        temp2.append(temp1[j:j + one_word])
    if Counter(temp2) == words:
        res.append(i)
print(res)
