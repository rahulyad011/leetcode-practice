# https://leetcode.com/problems/number-of-islands/description/

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n= len(grid[0])
        def isvalid(x, y):
            return x>=0 and x<m and y>=0 and y<n

        def bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                currnode = queue.popleft()
                # visited.add(currnode)
                for move in moves:
                    x_new = currnode[0] + move[0]
                    y_new = currnode[1] + move[1]
                    if isvalid(x_new, y_new) and grid[x_new][y_new]=='1':
                        queue.append((x_new, y_new))
                        grid[x_new][y_new]='0'
        
        count=0
        for i in range(m):
            for j in range(n):
                # print(sorted(visited))
                if grid[i][j]=='1':
                    bfs((i, j))
                    count+=1
                    grid[i][j]='0'
        return count


        