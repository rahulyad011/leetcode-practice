class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Solution:
        find the window of low and high having max difference, 
        if low updated then update high as well as high can be ahead or equal day to low
        """
        max_profit = 0
        low = 100000
        high = 0
        for price in prices:
            if price < low:
                low = price
                high = low
            if price > high:
                high = price
            max_profit = max(max_profit, high-low)
        return max_profit


        