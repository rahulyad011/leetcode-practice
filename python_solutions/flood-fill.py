from collections import deque

class Solution:
    """
    this problem can be solved by both bfs and dfs. Just handle the visited 
    condition properly otherwise it will go into TLE
    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def check_valid(a, b):
            if a<0 or b<0 or a>=len(image) or b>=len(image[0]):
                return False
            return True
        
        src_color = image[sr][sc]
        queue = deque()
        visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        # print(visited)
        def bfs(image, x, y, color):
            queue.append((x,y))
            while queue:
                ax, bx = queue.popleft()
                image[ax][bx] = color
                visited[ax][bx] = 1
                for neighbour in [(0,-1),(0,1),(1,0),(-1,0)]:
                    x_new = ax+neighbour[0]
                    y_new = bx+neighbour[1]
                    if check_valid(x_new, y_new):
                        if not visited[x_new][y_new] and image[x_new][y_new]==src_color :
                            queue.append((x_new, y_new))
                # print(image)
        bfs(image, sr, sc, color)
        return image