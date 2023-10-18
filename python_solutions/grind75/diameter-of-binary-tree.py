# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def depth(node):
            if node==None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        
        def diameterUtil(node):
            if node==None:
                return 
            self.diameter = max(self.diameter, (depth(node.left)+depth(node.right)))
        
        diameterUtil(root)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.diameter
        