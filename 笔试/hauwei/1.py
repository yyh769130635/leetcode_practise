# -*- encoding: utf-8 -*-
# @Time   : 2020/9/2 19:04
# @Author : Peter young
# @File   : 1.py

"""
输入是一个二维数组，"S" 代表是水 "H"代表是陆地  （注意里面存的是字符串，很坑 我调了半天才发现）
　　
　　从左上角(0, 0)开始 遍历所有位置 一直到右下角 (m, n)， 这个过程中
　　　　如果发现当前位置是"1"， 先把这个位置标记为查询过，
　　　　然后递归查看当前位置的上下左右四个位置，把是"1"的标记遍历过，再查看这个位置的上下左右
　　
　　实际上是一个循环 套了一个递归来实现。
　　当发现一个陆地 就计数器自增1 然后和这个陆地相连的所有陆地都标记为已经查找过

　　小技巧：
　　　　遍历图的时候，边界位置要留意，左边没有左侧，上边没有上侧，右边没有右侧，下边没有下侧，
　　　　　　可以写分支判断如果是边界就不遍历外侧。
　　　　我选择的办法是，在图的外侧增加一圈"S", 相当于扩大了整个图，
　　　　　　这样在递归陆地的过程中会节省了判断，并且不用考虑超出范围的问题。
"""

m = 4
n = 5
matrix = [["S", "S", "H", "H", "H"],
          ["S", "S", "H", "H", "H"],
          ["H", "H", "S", "H", "H"],
          ["H", "H", "H", "S", "S"]]

# m, n = map(int, input().split(","))
# matrix = []
# for i in range(m):
#     temp = []
#     string = input()
#     for j in range(n):
#         temp.append(string[j])
#     matrix.append(temp)

new_grid = [["H" for _ in range(n + 2)]]
for g in matrix:
    new_grid.append(["H"] + g + ["H"])
new_grid.append(["H" for _ in range(n + 2)])

num = 0  # 记录陆地数量


def deep_search(i, j, grid):
    """如果当前是陆地，把当前结点标记遍历过，并分别看左右上下四个位置"""
    if grid[i][j] == "H":
        return
    grid[i][j] = "H"
    deep_search(i - 1, j, grid)
    deep_search(i, j - 1, grid)
    deep_search(i, j + 1, grid)
    deep_search(i + 1, j, grid)


# 遍历除了周围的"0" 中间的部分
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if new_grid[i][j] == "S":  # 如果是陆地 就进入深度遍历
            num += 1
            deep_search(i, j, new_grid)

print(num)
