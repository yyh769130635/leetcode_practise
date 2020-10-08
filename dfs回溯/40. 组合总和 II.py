# -*- encoding: utf-8 -*-
# @Time   : 2020/10/6 21:17
# @Author : Peter young
# @File   : 40. 组合总和 II.py

class Solution:
    def combinationSum2(self, candidates, target):
        ans = []

        def dfs(candidates, path, target, index):
            if target == 0:
                ans.append(path)

            else:
                for i in range(index, len(candidates)):
                    if target - candidates[i] < 0:
                        break
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    dfs(candidates, path + [candidates[i]], target - candidates[i], i + 1)

        candidates.sort()
        dfs(candidates, [], target, 0)
        return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))