class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Learning1: We need to find the lowest and then the corresponding highest peaks 
        (please don't mistake it to global lowest and highest as high can only come after low(sell after buy))
        Learning2: as we can check the selling profit at each sell and compare to the maxprofit
        check whenever you see a peak from lowest point
        """

        if not prices:
            return 0
        lowest = prices[0]
        highest = 0
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                highest = price
                diff = highest - lowest
                max_profit = diff if diff > max_profit else max_profit
        return max_profit