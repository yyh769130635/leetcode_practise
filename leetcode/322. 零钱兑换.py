# -*- coding: utf-8 -*-
# @Time : 8/4/2020 1:53 PM
# @Author : Peter yang
coins = [1, 2, 5]
amount = 11
coins.sort(reverse=True)

# coins.sort(reverse=True)
# res = float("inf")
import sys

def main():

    res = sys.maxsize

    def dfs( coins, amount, temp):
        nonlocal res
        if amount == 0:
            res = min(res, len(temp))
            return
        if amount < 0:
            return
        for i in range(len(coins)):
            dfs(coins, amount - coins[i], temp + [coins[i]])


    dfs( coins, amount, [])
    print(res)

if __name__ == '__main__':
    main()

