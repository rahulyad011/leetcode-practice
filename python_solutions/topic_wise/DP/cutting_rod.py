#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        """recursive solution"""
        # def cutRodUtils(price, left, ind):
        #     if ind==0 or left==0:
        #         return 0
        #     if ind <= left:
        #         return max(cutRodUtils(price, left, ind-1) , price[ind-1]+cutRodUtils(price, left-ind, ind))
        #     else:
        #         return cutRodUtils(price, left, ind-1)
        # return cutRodUtils(price, n, n)
        
        """memorization solution - passes 1110/1115"""
        # length = n
        # dp = [[-1 for i in range(length+1)] for j in range(n+1)]
        # def cutRodUtils(price, ind, left):
        #     if ind==0 or left ==0 :
        #         dp[ind][left] = 0
        #         return dp[ind][left]
        #     if dp[ind][left] != -1:
        #         return dp[ind][left]
        #     if ind <= left:
        #         dp[ind][left] = max(cutRodUtils(price, ind-1, left ) , price[ind-1]+cutRodUtils(price, ind, left-ind))
        #         return dp[ind][left]
        #     else:
        #         dp[ind][left]= cutRodUtils(price, ind-1, left)
        #         return dp[ind][left]
        # return cutRodUtils(price, n, length)
        
        """top down solution with 2D dp - passes 1113/1115"""
        # # length = range(1, n+1)
        # dp = [[0 for i in range(n+1)] for j in range(n+1)]
        # # dp[i][j] where j represents the length of the rode and 
        # # i represents the current selected length(element)
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if i<= j:
        #             dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i][j-i ])
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[n][n] 
        
        """top down solution with 1D dp - passes all"""
        dp = [0] * (n + 1)
    
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i <= j:
                    dp[j] = max(dp[j], price[i - 1] + dp[j - i])
        return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
