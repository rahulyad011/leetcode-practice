# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Solution LCA4:
There can be three cases in this problem:
1. nodes on the left subtree and nodes on the right subtree, in this case we should return the roor itself
2. all nodes in the left substree, then we return left root
3. all nodes in the right subtree, then we return right root
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        LCS4 solution:
        
        """
        def dfs(root, nodes):
            if len(nodes)==1:
                return nodes[0]
            if not root:
                return None
            if root in nodes:
                return root
            l=dfs(root.left, nodes)
            r=dfs(root.right, nodes)

            if l and r:
                return root
            elif not r:
                return l
            else:
                return r
        return dfs(root, nodes)

        """
        Other solution:
        Below if the solution when the there are exactly two nodes in nodes list
        """
        # def dfs(node, node1, node2):
        #     if not node:
        #         return None
        #     if node == node1 or node == node2:
        #         return node
        #     l = dfs(node.left, node1, node2)
        #     r = dfs(node.right, node1, node2)

        #     if l and r:
        #         return node
        #     elif l:
        #         return l
        #     else:
        #         return r
        # return dfs(root, nodes[0], nodes[1])
        