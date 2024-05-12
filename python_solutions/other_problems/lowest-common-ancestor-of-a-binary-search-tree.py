# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Solution:
This is first type of the lowest ancestor series. Here tree is a BST so we can make these thre roles:
1. if first and second on left and right of the node then root is the return
2. if first and second is greater than root then we need to search in the right subtree
3. if first and second is smaller than root then we need to search in the left subtree
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, first, second):
            if not node:
                return None
            if node.val>=first and node.val<=second:
                return node
            if node.val<first and node.val<second:
                return dfs(node.right, first, second)
            if node.val>first and node.val>second:
                return dfs(node.left, first, second)
        if p.val >= q.val:
            first=q.val
            second=p.val
        else:
            first=p.val
            second=q.val
        return dfs(root, first, second)