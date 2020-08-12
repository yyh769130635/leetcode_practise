# -*- coding: utf-8 -*-
# @Time : 8/11/2020 3:53 PM
# @Author : Peter yang

def select_sort(d0):
    n = len(d0)
    l = 0
    while l < n:
        for i in range(l + 1, n):
            if d0[l] > d0[i]:
                d0[l], d0[i] = d0[i], d0[l]
        l += 1

    return d0


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d = []
    d1 = select_sort(d)
    # print(d1)
    # print(d0_out)
    print(d0_out == d1)
