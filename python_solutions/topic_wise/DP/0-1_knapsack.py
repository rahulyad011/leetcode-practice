#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # code here
        """
        recursive solution:
        """
        # # this base condition: least valid input(bag with no space and val)
        # if W==0 or n==0:
        #     return 0
        
        # #code choice function
        # # case 1 when weight of elment is more than the capacity available, 
        # # this means we can't take that item
        # if wt[n-1] > W:
        #     return self.knapSack(W, wt, val, n-1)
        # else:
        # # case 2 when weight of elment is more than the capacity available
        # # here we have two choices, either we can take the element or leave it
        #     return max(
        #         val[n-1]+self.knapSack(W-wt[n-1], wt, val, n-1),
        #         self.knapSack(W, wt, val, n-1)
        #         )
        
        """
        memorization solution:
        this means recursive calls with table
        size of table = size of the inputs that are changing in recursion
        in this case W and n
        """
        # table for DP:
        # using constrait of N and W for the size of table
        # dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        # def knapSack_util(W, wt, val, n):
        #     # this base condition: least valid input(bag with no space and val)
        #     if n==0 or W==0:
        #         return 0
        #     # change 1, check if the value was already calculated
        #     if dp[n][W] != -1:
        #         return dp[n][W]
        #     #code choice function
        #     # case 1 when weight of elment is more than the capacity available, 
        #     # this means we can't take that item
        #     if wt[n-1] > W:
        #         dp[n][W]=knapSack_util(W, wt, val, n-1)
        #         return dp[n][W]
        #     else:
        #     # case 2 when weight of elment is more than the capacity available
        #     # here we have two choices, either we can take the element or leave it
        #         dp[n][W]=max(
        #             val[n-1]+knapSack_util(W-wt[n-1], wt, val, n-1),
        #             knapSack_util(W, wt, val, n-1)
        #             )
        #         return dp[n][W]
        # return knapSack_util(W, wt, val, n)
        
        """
        Top Down DP Solution:
        this means solution using only the table no recursive calls
        """
        # table for DP:
        # using constrait of N and W for the size of table
        dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        
        # this base condition: least valid input(bag with no space and val)
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j]=0
                    
        # we will write the iterative solution similar to the recursive calls in memorization
        # each problem broken into multiple subproblems and solving these subproblems leads us 
        # to the solution
        for i in range(1, n+1):
            for j in range(1, W+1):
                #code choice function
                if wt[i-1] > j:
                # case 1 when weight of elment is more than the capacity available, 
                # this means we can't take that item
                    dp[i][j] = dp[i-1][j]
                else:
                # case 2 when weight of elment is more than the capacity available
                # here we have two choices, either we can take the element or leave it
                    dp[i][j] = max(dp[i-1][j], (val[i-1] + dp[i-1][j-wt[i-1]]))
        
        return dp[n][W]
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends