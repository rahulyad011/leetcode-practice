class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Learning: welcome to DP, this is simple linear DP where
        heart of DP is dp[i] = dp[i-1] + dp[i-2],meaning the step count at ith
        height depends on i-1 and i-2 height's step count
        """
        """recursion"""
        # def climbUtil(top):
        #     if top == 0:
        #         return 1
        #     if top <0:
        #         return 0
        #     return climbUtil(top-1) + climbUtil(top-2)
        # return climbUtil(n)

        """DP with Memorizaiton"""
        # dp = [-1]*(n+1)
        # def climbUtil(top):
        #     if top == 0:
        #         dp[top] = 1
        #         return dp[top]
        #     if top < 0:
        #         dp[top] = 0
        #         return dp[top]
        #     if dp[top]!=-1:
        #         return dp[top]
        #     else:
        #         dp[top] = climbUtil(top-1) + climbUtil(top-2)
        #         return dp[top]
        # return climbUtil(n)

        """DP top down"""
        dp = [0]*(n+1)
        dp[0] = 1
        if n>0:
            dp[1] = 1
        if n>1:
            dp[2] = 2
        for i in range(2, n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]