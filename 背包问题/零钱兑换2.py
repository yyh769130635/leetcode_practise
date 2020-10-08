# -*- encoding: utf-8 -*-
# @Time   : 2020/10/6 20:42
# @Author : Peter young
# @File   : 零钱兑换2.py

class Solution:
    def change(self, amount: int, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


amount = 5
coins = [1, 2, 5]
s = Solution()
print(s.change(amount, coins))
