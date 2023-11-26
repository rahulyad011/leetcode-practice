class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Solution:
        This is a variation of 0/1 knapsack problem espically subset sum problem
        because if we closedly observe then the positive se tof number is a subset the sum of 
        this subset is know can can be calculate by below equations:
        pos + neg = total 
        and 
        pos - neg= target
        pos = target + total /2
        important edge cases:
        1. zeroes present in array
        here one more important change is that we don't stop the recusion at postive_sum==0 because 
        there can be zeroes in the array and those zeroes can also make multiple combination.
        So base condition is modified to positive_sum<0 and n==0
        2. only negative value present in the array:
        here we just check if the target sum is equal to the negative sum and return 1 in that case
        """
        total = sum(nums)
        positive_sum = 0
        if (target + total) % 2:
            return 0
        else:
            positive_sum = int((target + total) / 2)

        """recursive solution: timeout"""
        # n = len(nums)
        # def countWaysSubsetsum(positive_sum, n):
        #     if positive_sum < 0:
        #         return 0
        #     if n == 0:
        #         if positive_sum == 0:
        #             return 1
        #         else:
        #             return 0
        #     if nums[n-1] > positive_sum:
        #         return countWaysSubsetsum(positive_sum, n-1)
        #     else:
        #         return countWaysSubsetsum(positive_sum, n-1) + countWaysSubsetsum(positive_sum-nums[n-1], n-1)
        # return countWaysSubsetsum(positive_sum, n) 
        
        """top down solution"""
        if positive_sum < 0:
            # as according to the constraits sum and nums is always positive
            return 0

        n = len(nums)
        dp = [[0 for i in range(positive_sum+1)] for j in range(n+1)]

        dp[0][0] = 1

        for j in range(1, n+1):
            for i in range(positive_sum+1):
                if nums[j-1] > i:
                    dp[j][i] = dp[j-1][i]
                else:
                    dp[j][i] = dp[j-1][i-nums[j-1]] + dp[j-1][i]
        return dp[n][positive_sum]
