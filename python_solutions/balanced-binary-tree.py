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
        def depth(head):
            if not head:
                return 0
            left_height = depth(head.left)
            right_height = depth(head.right)
            return max(left_height, right_height) + 1
        if abs(depth(root.left) - depth(root.right)) <=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        