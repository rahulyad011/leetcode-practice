from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Solution:
        It is a bfs solution but visited set is not required 
        because the color change be used to track the node visit

        DFS can be faster here can we won't need queue in DFS can save some space
        """

        if image[sr][sc] == color:
            return image
        m = len(image)
        n = len(image[0])
        def isvalid(x, y):
            return m>x>=0 and n>y>=0
        queue = deque()
        # visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        src_color = image[sr][sc]
        def bfs(start):
            while queue:
                a,b = queue.pop()
                # visited.add((a, b))
                for move in moves:
                    x_new = a+move[0]
                    y_new = b+move[1]
                    if isvalid(x_new, y_new) and image[x_new][y_new] == src_color:
                        image[x_new][y_new] = color
                        queue.append((x_new, y_new))
        
        image[sr][sc] = color
        queue.append((sr, sc))
        bfs((sr,sc))
        return image