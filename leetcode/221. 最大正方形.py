# -*- encoding: utf-8 -*-
# @Time   : 2020/9/1 15:21
# @Author : Peter young
# @File   : 221. 最大正方形.py
# matrix = [[1, 0, 1, 0, 0],
#           [1, 0, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 0, 0, 1, 0]]


matrix = [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]
m = len(matrix)
n = len(matrix[0])
# if n <= 1 or m <= 1:
#     return min(n, m)
dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    dp[0][i] = int(matrix[0][i])
for i in range(m):
    dp[i][0] = int(matrix[i][0])

for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == "1":
            if dp[i - 1][j - 1] == 0 or dp[i - 1][j] == 0 or dp[i][j - 1] == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
Max = dp[0][0]
for i in range(m):
    for j in range(n):
        Max = max(dp[i][j], Max)
print(Max)
