class Solution:
    def minDifference(self, arr, n):
        """Top Down DP"""
        def subsetSum(n, arr, target):
            dp = [[False for i in range(target+1)] for j in range(n+1)]
            for i in range(n+1):
                dp[i][0] = True
            
            for i in range(1, n+1):
                for j in range(1, target+1):
                    if arr[i-1] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            return dp
        
        total = sum(arr)
        first_half = int(total/2)
        second_half = None
        
        # this condition is for the test case where the len(arr)=1, means min diff = arr[0]
        if len(arr) == 1:
            return arr[0]
        
        diff = 0
        result_array = subsetSum(n, arr, first_half)
        while first_half:
            if not result_array[n][first_half]:
                first_half -= 1
            else:
                second_half = total - first_half
                diff = second_half - first_half
                return diff
        
        return diff

# Driver Code
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)
# } Driver Code Ends
