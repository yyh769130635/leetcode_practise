# -*- encoding: utf-8 -*-
# @Time   : 2020/9/10 14:19
# @Author : Peter young
# @File   : 剑指 Offer 12. 矩阵中的路径.py

class Solution:
    def exist(self, board, word) -> bool:
        m = len(board)
        if m < 1:
            return False
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, visited, word, board):
                        return True
        return False

    def dfs(self, i, j, visited, word, board):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] == 1 or board[i][j] != word[0]:
            return False
        visited[i][j] = 1
        res = self.dfs(i + 1, j, visited, word[1:], board) or self.dfs(i - 1, j, visited, word[1:], board) or self.dfs(
            i, j + 1, visited, word[1:], board) or self.dfs(i, j - 1, visited, word[1:], board)
        visited[i][j] = 0
        return res


solution = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(solution.exist(board, word))