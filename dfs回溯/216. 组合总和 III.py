# -*- encoding: utf-8 -*-
# @Time   : 2020/10/7 15:58
# @Author : Peter young
# @File   : 216. 组合总和 III.py

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(path, target, index):
            if len(path)==k:
                if target==0:
                    ans.append(path)
                return
            for i in range(index,10):
                if i>target:
                    break
                dfs(path+[i],target-i,i+1)

        dfs([], n, 1)
        return ans