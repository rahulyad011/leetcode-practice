# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        learning1:
        case1: p and q both on right side of root
        case2: p and q both on left side of root
        case3: p and q both on opposite side of root
        """
        if root != None:
            # case1: p and q both on right side of root
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            # case2: p and q both on left side of root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            # case3: p and q both on opposite side of root
            else:
                return root