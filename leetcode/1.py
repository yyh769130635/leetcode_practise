# -*- coding: utf-8 -*- #
# @Time   : 2020/8/28 21:46
# @Author : Peter young
# @File   : 1.py


class Solution:
    def exist(self, board, word):
        r = len(board)
        c = len(board[0])
        if r == 0 or c == 0:
            return False
        visited = [[0 for i in range(c)] for j in range(r)]
        L = len(word)

        def dfs(i, j, cur, visited):
            if cur == L :
                return True
            if i < 0 or i >= r or j < 0 or j >= c or visited[i][j] == 1 or board[i][j] != word[cur]:
                return False
            visited[i][j] = 1
            res = dfs(i + 1, j, cur + 1, visited) or dfs(i - 1, j, cur + 1, visited) or dfs(i, j + 1, cur + 1, visited) or dfs(i, j - 1, cur + 1, visited)
            visited[i][j] = 0
            return res

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, visited):
                        return True
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
ans = s.exist(board,word)
print(ans)