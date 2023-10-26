# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
        solution1: recursive 
        root.left, root.right needs to be swapped,
        this can be down at the start of the recursive or at 
        the end while making a return
        """
        # if not root:
        #     return None
        # # recursive switch the left and right child of each node
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        # # time complexity O(n) reaching all nodes atleast once
        # space complexity O(h) h is the height of the tree which is actually O(n)

        """
        Solution2 : iterative
        this is a BFS solution where we swap the nodes before append in the queue
        """
        
        # queue = deque()
        # queue.append(rootN)
        # while queue:
        #     head = queue.popleft()
        #     temp = head.left
        #     head.left =  head.right
        #     head.right = temp
        #     if head.left:
        #         queue.append(head.left)
        #     if head.right:
        #         queue.append(head.right)
        # return rootN


        """
        Recursion with better explaining print statements
        (must watch once to revise recursion)
        """
        if root == None:
            return root
        else:
            print("before left:", root.val)
            self.invertTree(root.left)
            print("before right:", root.val)
            self.invertTree(root.right)
            print("after right:", root.val)
            temp = root.left
            root.left =  root.right
            root.right = temp
        return root