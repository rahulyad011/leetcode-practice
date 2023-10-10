# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """sol1 recusive solution"""
        # def lcsUtil(text1, text2, n, m):
        #     if n==0 or m==0:
        #         return 0
        #     if text1[n-1]==text2[m-1]:
        #         return 1+lcsUtil(text1, text2, n-1, m-1)
        #     else:
        #         return max(lcsUtil(text1, text2, n-1, m), lcsUtil(text1, text2, n, m-1))
        # return lcsUtil(text1, text2, len(text1), len(text2))

        """sol2 bottom up DP(memorization) solution"""
        # dp = [[-1 for i in range(len(text1)+1)] for i in range(len(text2)+1)]
        # def lcsUtil(text1, text2, n, m):
        #     if n==0 or m==0:
        #         dp[m][n] = 0
        #         return 0
        #     if dp[m][n] != -1:
        #         return dp[m][n]
        #     if text1[n-1]==text2[m-1]:
        #         dp[m][n] = 1+lcsUtil(text1, text2, n-1, m-1)
        #         return dp[m][n]
        #     else:
        #         dp[m][n] = max(lcsUtil(text1, text2, n-1, m), lcsUtil(text1, text2, n, m-1))
        #         return dp[m][n]
        # return lcsUtil(text1, text2, len(text1), len(text2))

        """sol3 top down DP solution"""
        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            dp[0][i]= 0
        for j in range(m+1):
            dp[j][0]= 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]