# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
Solution LCA3:
For this problem first we need to find the root of the tree using the parent connections
To do it in one run we first do the LCA run and then check with the results
There can be three cases in this problem:
1. nodes on the left subtree and nodes on the right subtree, in this case we should return the roor itself
2. all nodes in the left substree, then we return left root
3. all nodes in the right subtree, then we return right root
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        curr = p
        while curr.parent:
            if curr == q:
                return curr
            else:
                curr = curr.parent
        # print(curr.val)

        def lcaUtils(root, node1, node2):
            if not root or root==node1 or root==node2:
                return root
            ltree = lcaUtils(root.left, node1, node2)
            rtree = lcaUtils(root.right, node1, node2)
            if ltree and rtree:
                return root
            elif ltree:
                return ltree
            else:
                return rtree

        return lcaUtils(curr, p, q)

        """soution2:
        Iterative solution: keeping the parents of p in a parent set and then compare with run by q -> q.parent..
        """