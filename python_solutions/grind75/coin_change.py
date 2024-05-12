# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        int_max = 100000
        """Recursive solution"""
        # def coinChangeUtil(coins, n , amount):
        #     if amount==0:
        #         return 0
        #     if n==0:
        #         if amount!=0:
        #             return int_max
        #     if coins[n-1]>amount:
        #         return coinChangeUtil(coins, n-1, amount)
        #     else:
        #         return min(coinChangeUtil(coins, n-1, amount), 1 + coinChangeUtil(coins, n, amount-coins[n-1]))
        # n = len(coins)
        # result = coinChangeUtil(coins, n, amount)
        # if result == int_max:
        #     return -1
        # else:
        #     return result

        """memorization with dp - all testcases passing"""
        # dp = None
        # def coinChangeUtil(coins, n , amount):
        #     if amount==0:
        #         dp[n][amount] = 0
        #         return dp[n][amount]
        #     if n==0:
        #         if amount!=0:
        #             dp[n][amount]=int_max
        #             return dp[n][amount]
        #     if dp[n][amount]!=-1:
        #         return dp[n][amount]
        #     if coins[n-1]>amount:
        #         dp[n][amount] = coinChangeUtil(coins, n-1, amount)
        #         return dp[n][amount]
        #     else:
        #         dp[n][amount] = min(coinChangeUtil(coins, n-1, amount), 1 + coinChangeUtil(coins, n, amount-coins[n-1]))
        #         return dp[n][amount]
        # n = len(coins)
        # dp = [[-1 for i in range(amount+1)] for j in range(n+1)]
        # result = coinChangeUtil(coins, n, amount)
        # if result == int_max:
        #     return -1
        # else:
        #     return result

        """Top down DP approach 2D dp -- passes all test cases"""
        n = len(coins)
        dp = [[0 for i in range(amount+1)] for i in range(n+1)]

        for i in range(amount+1):
            # first row i.e n=0
            dp[0][i] = int_max

        for i in range(n+1):
            #first column i.e amount=0
            dp[i][0] = 0 
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[n][amount]!=int_max:
            return dp[n][amount]
        else:
            return -1

        """Top down DP approach 1D dp -- fastest"""

        # for revision work


        