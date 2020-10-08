# -*- encoding: utf-8 -*-
# @Time   : 2020/10/7 15:15
# @Author : Peter young
# @File   : 面试题 04.01. 节点间通路.py

class Solution:
    def findWhetherExistsPath(self, n: int, graph, start: int, target: int) -> bool:
        visited = [False] * n
        visited[start] = True
        for i in range(len(graph)):
            nums = graph[i]
            if visited[nums[0]]:
                visited[nums[1]] = True

        return visited[target]


s = Solution()
print(s.findWhetherExistsPath(5, [[3, 4], [0, 1], [1, 2], [1, 3]], 0, 4))
