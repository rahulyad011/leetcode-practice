# https://leetcode.com/problems/construct-product-matrix/description/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """Solution1: 
        Using Prefix and Suffix Matrix of same size as Grid
        Don't try to use lot of matrices else it will give TLE"""
        prev_prod = 1
        n = len(grid)
        m = len(grid[0])
        prev_prod_suf = 1
        prefix = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
        suffix = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
        n = len(grid)
        m = len(grid[0])
        # p = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prefix[i][j] = prev_prod
                prev_prod = (prev_prod*grid[i][j])%12345

                suffix[n-1-i][m-1-j] = prev_prod_suf
                prev_prod_suf = (prev_prod_suf * grid[n-1-i][m-1-j])%12345
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=(prefix[i][j]*suffix[i][j])%12345
        return grid

        """Solution2(Optimal): 
        Using List for prefix and suffix instead of matrix, this will be faster
        (Try later)
        """
        
                
            
        