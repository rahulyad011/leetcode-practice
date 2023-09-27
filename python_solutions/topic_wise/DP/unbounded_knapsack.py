#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        dp= [[-1 for i in range(W+1)] for j in range(N+1)]
        
        """memorization DP solution"""
        # def knapSackUtil(N, W, val, wt):
        #     # code here
        #     if N==0 or W==0:
        #         return 0
            
        #     if dp[N][W] != -1:
        #         return dp[N][W]
            
        #     if wt[N-1] > W:
        #         dp[N][W] = knapSackUtil(N-1, W, val, wt)
        #         return dp[N][W]
        #     else:
        #         dp[N][W] = max(knapSackUtil(N-1, W, val, wt), val[N-1] + knapSackUtil(N, W-wt[N-1], val, wt))
        #         return dp[N][W]
        # return knapSackUtil(N, W, val, wt)
        
        """Top Down DP solution"""
        # # initialization
        # # type 1 initialization 
        for i in range(N+1):
            for j in range(W+1):
                if i==0 or j==0:
                    dp[i][j]=0
        # # type 2 initialization
        # for j in range(W+1):
        #         dp[0][j]=0
        # for i in range(N+1):
        #         dp[i][0]=0
        for j in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i][j-wt[i-1]])
        
        return dp[N][W]
        
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends