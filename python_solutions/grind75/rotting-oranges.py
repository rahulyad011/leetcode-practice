# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Solution Inspiration 01 matrix problem
        if the we can identify the min distance of non 
        rotten oranges from rotten oranges, the max of these distance will be the
        time when all can become rotten
        """
        m = len(grid)
        n = len(grid[0])
        def isvalid(x, y):
            return m>x>=0 and n>y>=0
        queue = deque()
        count_nrot=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j]=-2
                elif grid[i][j]==1:
                    grid[i][j]=10000
                    count_nrot+=1
                else:
                    grid[i][j]=0
                    queue.append((i, j))
        if count_nrot == 0:
            return 0
        if len(queue) == 0:
            return -1
        
        # visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            a, b = queue.popleft()
            for move in moves:
                x_new = a + move[0]
                y_new = b + move[1]
                if isvalid(x_new, y_new) and grid[x_new][y_new]!=0:
                    if grid[x_new][y_new] > grid[a][b]+1:
                        grid[x_new][y_new] = grid[a][b]+1
                        queue.append((x_new, y_new))
        
        max_time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 10000:
                    return -1
                max_time = max(max_time, grid[i][j])
        
        return max_time


        """
        Alternate solution: keep parent counter in the queue tuple, 
        this will give us the time when each of orange gets rotten
        or we increment the count on each time iteration update
        """



        