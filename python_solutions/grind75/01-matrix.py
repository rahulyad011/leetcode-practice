from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        def isvalid(x, y):
            return x>=0 and x<n and y>=0 and y<m 
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]!=0:
                    mat[i][j]='*'
                else:
                    queue.append((i, j))
        
        while queue:
            # print(queue)
            i, j = queue.popleft()
            for move in moves:
                x_new = i + move[0]
                y_new = j + move[1]
                if isvalid(x_new, y_new) and mat[x_new][y_new]!=0:
                    if mat[x_new][y_new]=='*':
                        mat[x_new][y_new] = mat[i][j]+1
                        queue.append((x_new, y_new))
                    else:
                        if mat[x_new][y_new] > mat[i][j]+1:
                            mat[x_new][y_new] = mat[i][j]+1
                            queue.append((x_new, y_new))
        return mat


        