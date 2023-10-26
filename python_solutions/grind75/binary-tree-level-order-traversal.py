from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        def bfs(node):
            if not node:
                return result
            queue.append((node, 0))
            while queue:
                parent,level  = queue.popleft()
                if len(result)<level+1:
                    result.append([])
                result[level].append(parent.val)
                if parent.left:
                    queue.append((parent.left, level+1))
                if parent.right:
                    queue.append((parent.right, level+1))
        bfs(root)

        return result

            
            