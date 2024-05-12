# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Solution LCA2:
For this problem first we need to check if the given nodes p and q exist in the tree or not. If exist then we follow LCA1 pattern as it is
To do it in one run we first do the LCA run and then check with the results
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
            if node == node1 or node == node2:
                return node
            lefttree = lcaUtil(node.left, node1, node2)
            righttree = lcaUtil(node.right, node1, node2)
            if lefttree and righttree:
                return node
            elif not righttree:
                return lefttree
            else:
                return righttree
            return node1

        def checkExistence(node, targetnode):
            if not node:
                if not targetnode:
                    return True
                else:
                    return False
            if node == targetnode:
                return True
            return checkExistence(node.left, targetnode) or checkExistence(node.right, targetnode)
        
        found = lcaUtil(root, p, q)
        if not found:
            return None
        if found == p:
            if checkExistence(p, q):
                return p
            else:
                return None
        elif found == q:
            if checkExistence(q, p):
                return q
            else:
                return None
        else:
            return found
        
        