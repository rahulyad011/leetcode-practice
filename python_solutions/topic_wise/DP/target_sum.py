class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def countSubsetSum(n, arr, target_sum):
            if target_sum < 0:
                return 0
            dp = [[0 for i in range(target_sum+1)] for j in range(n+1)]
            # this for the 
            dp[0][0] = 1
            for i in range(1, n+1):
                for j in range(target_sum+1):
                    if arr[i-1] > target_sum:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            return dp[n][target_sum]
        total = sum(nums)
        # sum of positive + negative numbers == sum-difference
        diff = target
        # s1 + s2 = total and s1-s2=diff , s1= total+diff/2
        comb = total + diff
        if comb%2:
            return 0
        else:
            s1 = int(comb/2)
            n = len(nums)
            return countSubsetSum(n, nums, s1)

                    
            
        