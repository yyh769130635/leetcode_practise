# -*- encoding: utf-8 -*-
# @Time   : 2020/8/30 20:52
# @Author : Peter young
# @File   : 77.组合.py

n = 4
k = 2
res = []


def dfs(start, temp):
    global res
    if len(temp) == k:
        res.append(temp)
        return
    for i in range(start, n + 1):
        dfs(i + 1, temp + [i])
dfs(1,[])

print(res)
