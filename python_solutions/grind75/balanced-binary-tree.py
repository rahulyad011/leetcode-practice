# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Learning 1: It is an extension of height of tree problem, so can reuse 
        the height calculation(i.e. max(left_tree, right_tree)+1) code again
        Learning 2:
        should not return true for the balanced tree until we recurively 
        checked all the below nodes
        """
        if not root:
            return True

        def depth(node):
            if not node:
                return 1
            return max(1+depth(node.left), 1+depth(node.right))

        def checkbalance(node):
            if not node:
                return True
            diff = abs(depth(node.left)-depth(node.right)) <= 1
            return diff and checkbalance(node.left) and checkbalance(node.right)
        
        return checkbalance(root)