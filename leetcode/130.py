# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 19:46
# @Author : Peter young
# @File   : 130.py
# board = [["X","X","X","X"],
#          ["X","O","O","X"],
#          ["X","X","O","X"],
#          ["X","O","X","X"],]
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
# if not board:
#     return
q = []
m, n = len(board), len(board[0])
for i in range(m):
    if board[i][0]=="O":
        q.append([i, 0])
    if board[i][n - 1]=="O":
        q.append([i, n - 1])
for j in range(n):
    if board[0][j]=="O":
        q.append([0, j])
    if board[m - 1][j]=="O":
        q.append([m - 1, j])
print(q)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    temp = q.pop(0)
    i = temp[0]
    j = temp[1]
    board[i][j] = "A"
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
            q.append([x, y])

for i in range(m):
    for j in range(n):
        if board[i][j] == "O":
            board[i][j] = "X"
        elif board[i][j] == "A":
            board[i][j] = "O"
print(board)