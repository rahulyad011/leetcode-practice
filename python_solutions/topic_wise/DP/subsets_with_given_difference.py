#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPartitions(self, n, d, arr):
        total = sum(arr)
        comb = total + d
        target = 0
        if comb % 2 or comb < 0:
            return 0
        else:
            target = int(comb/2)
        dp = [[0 for i in range(target+1)] for j in range(n+1)]
        # the first element of the first column = 1 (empty set)
        dp[0][0]=1
        def subsetsum(n, arr, target):
            for i in range(1, n+1):
                # please note that here we are starting from 0th column because there be subset of zeroes
                # eg : {}, {0}, {0, 0}
                for j in range(0, target+1):
                    if arr[i-1]>j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]])
            return dp[n][target]
            
        return subsetsum(n, arr, target) % (pow(10, 9) + 7)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends