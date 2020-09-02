# -*- encoding: utf-8 -*-
# @Time   : 2020/8/31 19:34
# @Author : Peter young
# @File   : 994.py

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
rotlist = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            rotlist.append([i, j])
time = 0
while rotlist:
    newrotlist = []
    for rotnode in rotlist:
        a = rotnode[0]
        b = rotnode[1]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                grid[x][y] = 2
                newrotlist.append([x, y])
    if not newrotlist:
        break
    rotlist[:] = newrotlist[:]
    time += 1
print(grid)