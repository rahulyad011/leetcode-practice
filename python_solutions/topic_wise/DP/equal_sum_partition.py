# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        total = sum(arr)
        cols = int(total/2)
        dp = [[-1 for i in range(cols+1)] for j in range(N+1)]
        def subsetsum(N, nums, target_sum):
            """Top Down/Memo solution base conditions"""
            for i in range(N+1):
                for j in range(target_sum+1):
                    # there are no numbers
                    if i == 0:
                        dp[i][j] = False
                    # target sum is 0
                    if j == 0:
                        dp[i][j] = True
            """recursive solution base conditions"""
            # if not target_sum:
            #     return True
            # if not N:
            #     return False
            
            """Memo check if already exist condition"""
            # if dp[N][target_sum]!=-1:
            #     return dp[N][target_sum]
            # """memo recursive condition"""
            # if nums[N-1]>target_sum:
            #     dp[N][target_sum] = subsetsum(N-1, nums, target_sum)
            #     return dp[N][target_sum]
            # else:
            #     dp[N][target_sum] = subsetsum(N-1, nums, target_sum) or subsetsum(N-1, nums, target_sum-nums[N-1])
            #     return dp[N][target_sum]
            
            """Top Down solution"""
            for i in range(1, N+1):
                for j in range(1, target_sum+1):
                    if nums[i-1] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            return dp[N][target_sum]
            
        if not total%2:
            return subsetsum(N, arr, int(total/2))
        else:
            return False
            

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends