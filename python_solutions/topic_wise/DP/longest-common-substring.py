#User function Template for python3
# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        """sol1 recursion"""
        # def lcSubstrUtil(S1, S2, n, m, maxlen):
        #     if n==0 or m==0:
        #         return maxlen
        #     if S1[n-1] == S2[m-1]:
        #         maxlen = lcSubstrUtil(S1, S2, n-1, m-1, maxlen+1)
        #     else:
        #         maxlen = max(maxlen, max(lcSubstrUtil(S1, S2, n-1, m, 0), lcSubstrUtil(S1, S2, n, m-1, 0)))
        #     return maxlen
        # return lcSubstrUtil(S1, S2, n, m, maxlen=0)
        
        
        """the below solution is incorrect"""
        """sol2 memorization"""
        # dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        # def lcSubstrUtil(S1, S2, n, m, maxlen):
        #     if n==0 or m==0:
        #         dp[n][m] = maxlen
        #         return dp[m][n]
        #     if dp[n][m] != -1:
        #         return dp[n][m]
        #     if S1[n-1] == S2[m-1]:
        #         maxlen = lcSubstrUtil(S1, S2, n-1, m-1, maxlen+1)
        #         dp[n][m] = maxlen
        #     else:
        #         maxlen = max(maxlen, max(lcSubstrUtil(S1, S2, n-1, m, 0), lcSubstrUtil(S1, S2, n, m-1, 0)))
        #         dp[n][m] = maxlen
        #     return dp[n][m]
        # return lcSubstrUtil(S1, S2, n, m, maxlen=0)
        
        
        """sol3 top down"""
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        result = 0
        def lcSubstrUtil(S1, S2, n, m, result):
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if S1[i-1] == S2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                        result = max(result, dp[i][j])
                    else:
                        dp[i][j] = 0
            return result
        return lcSubstrUtil(S1, S2, n, m, result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends