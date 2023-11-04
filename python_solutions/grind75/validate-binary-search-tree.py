# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Solution: 
        When we for the left side of the tree, we just extra condition:
        that is max of left.val  < root.val
        for the min condition it is the same as the condition on the root node
        simiarly for the right node, the new condition will be the minimum of
        i.e right.val > root.val 
        for max condition it is the same as for the root node
        because if A>B and B>C then A>C
        """
        INT_MAX = pow(2,31)+1
        INT_MIN = -pow(2,31)-1
        def dfsBST(node, minval, maxval):
            if not node:
                return True
            # print(node.val, minval, maxval)
            if minval >= node.val or maxval <= node.val:
                return False
            return dfsBST(node.left, minval, node.val) and dfsBST(node.right, node.val, maxval)
        return dfsBST(root, INT_MIN, INT_MAX)