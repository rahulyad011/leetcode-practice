#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        """recursion"""
        # if sum == 0:
        #     return True
        # if N==0 and sum!=0:
        #     return False
        
        # if arr[N-1] > sum:
        #     return self.isSubsetSum(N-1, arr, sum)
        # else:
        #     return self.isSubsetSum(N-1, arr, sum) or self.isSubsetSum(N-1, arr, sum-arr[N-1])
        
        """Memo DP"""
        dp = [[-1 for i in range(sum+1)] for j in range(N+1)]
        def isSubsetSumUtil(N, arr, sum):
            # code here 
            if sum==0:
                dp[N][sum]=True
                return True
            if N==0 and sum!=0:
                dp[N][sum]=False
                return False
            if dp[N][sum]!=-1:
                return dp[N][sum]
            
            if arr[N-1]<=sum:
                dp[N][sum] = isSubsetSumUtil(N-1, arr, sum - arr[N-1]) or isSubsetSumUtil(N-1, arr, sum)
                return dp[N][sum]
            else:
                dp[N][sum]=isSubsetSumUtil(N-1, arr, sum)
                return dp[N][sum]
        return isSubsetSumUtil(N, arr, sum)
        
        """Topdown DP"""
        dp = [[False for j in range(sum+1)] for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = True
        for i in range(1, N+1):
            for j in range(1, sum+1):
                if arr[i-1]> j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
        return dp[N][sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends