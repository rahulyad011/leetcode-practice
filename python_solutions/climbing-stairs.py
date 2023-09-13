class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Learning: welcome to DP, this is simple linear DP where
        heart of DP is dp[i] = dp[i-1] + dp[i-2],meaning the step count at ith
        height depends on i-1 and i-2 height's step count
        """
        steps=[0 for i in range(n+1)]
        steps[0] = 0
        if n<=2:
            return n
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n+1):
            steps[i]= steps[i-1] + steps[i-2]
        return steps[n]

        """
        recursive equation which goes in TLE for larger height
        """
        # if n<=2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)