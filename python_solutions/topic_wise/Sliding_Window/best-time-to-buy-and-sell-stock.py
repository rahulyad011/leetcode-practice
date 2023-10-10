# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices)<=1:
            return max_profit
        l = 0
        r = 1
        while r < len(prices):
            if prices[r]-prices[l] > max_profit:
                max_profit = prices[r]-prices[l]
            else:
                if prices[l] > prices[r]:
                    l=r
            r+=1
        return max_profit