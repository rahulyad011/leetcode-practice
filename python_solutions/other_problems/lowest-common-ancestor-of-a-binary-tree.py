# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Solution LCA1:
There can be three cases in this problem:
1. nodes on the left subtree and nodes on the right subtree, in this case we should return the roor itself
2. all nodes in the left substree, then we return left root
3. all nodes in the right subtree, then we return right root
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcaUtil(node, node1, node2):
            if not node:
                return None
            if node==node1 or node==node2:
                return node
            left = lcaUtil(node.left, node1, node2)
            right = lcaUtil(node.right, node1, node2)

            if left and right:
                return node
            elif not right:
                return left
            else:
                return right
        
        return lcaUtil(root, p, q)