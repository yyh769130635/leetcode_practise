# -*- encoding: utf-8 -*-
# @Time   : 2020/9/12 20:08
# @Author : Peter young
# @File   : vivo.py
"""
迷宫的最短路径之BFS算法（python实现）

"""
from collections import deque

MAX_VALUE = float('inf')


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def bfs(maze, begin, end):
    n, m = len(maze), len(maze[0])
    dist = [[MAX_VALUE for _ in range(m)] for _ in range(n)]
    pre = [[None for _ in range(m)] for _ in range(n)]  # 当前点的上一个点,用于输出路径轨迹

    dx = [1, 0, -1, 0]  # 四个方位
    dy = [0, 1, 0, -1]
    sx, sy = begin.x, begin.y
    gx, gy = end.x, end.y

    dist[sx][sy] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        curr = queue.popleft()
        find = False
        for i in range(4):
            nx, ny = curr.x + dx[i], curr.y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and dist[nx][ny] == MAX_VALUE:
                dist[nx][ny] = dist[curr.x][curr.y] + 1
                pre[nx][ny] = curr
                queue.append(Point(nx, ny))
                if nx == gx and ny == gy:
                    find = True
                    break
        if find:
            break
    # print('最短路径的长度：')
    print(dist[gx][gy])

    # print('最短路径轨迹（之一）：')
    # stack = []
    # curr = end
    # while True:
    #     stack.append(curr)
    #     if curr.x == begin.x and curr.y == begin.y:
    #         break
    #     prev = pre[curr.x][curr.y]
    #     curr = prev
    # while stack:
    #     curr = stack.pop()
    #     print('(%d, %d)' % (curr.x, curr.y))


if __name__ == '__main__':

    n = int(input())
    zuobiao = list(map(int, input().split(" ")))

    begin = Point(zuobiao[0], zuobiao[1])
    end = Point(zuobiao[2], zuobiao[3])

    maze = []
    for i in range(n):
        s = input()
        maze.append(list(s))
    bfs(maze, begin, end)
