# -*- encoding: utf-8 -*-
# @Time   : 2020/10/6 20:32
# @Author : Peter young
# @File   : 找零钱.py

class Solution(object):
    def coinChange(self, coins, amount):
        res = [float('inf') for _ in range(amount + 1)]
        for i in coins:
            if i<len(res):
                res[i] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    if res[i - coin] == float('inf'):
                        continue
                    else:
                        res[i] = min(res[i - coin] + 1, res[i])
        print(res)
        if res[-1] == float('inf'):
            return -1
        else:
            return res[-1]


amount = 11
coins = [1, 2, 5]
s = Solution()
print(s.coinChange(coins, amount))
