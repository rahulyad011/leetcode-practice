# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # """
        # Learning 1: It is an extension of height of tree problem, so can reuse 
        # the height calculation(i.e. max(left_tree, right_tree)+1) code again
        # Learning 2:
        # should not return true for the balanced tree until we recurively 
        # checked all the below nodes
        # """
        # if not root:
        #     return True
        # def depth(head):
        #     if not head:
        #         return 0
        #     left_height = depth(head.left)
        #     right_height = depth(head.right)
        #     return max(left_height, right_height) + 1
        # if abs(depth(root.left) - depth(root.right)) <=1:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        # else:
        #     return False

        def balancedUtils(node):
            """
            this is not exactly the depth related solution:
            because here we use depth calculation but we need to save it so that we can avoid calculating at each node

            in a bottom to up recursive fashion we check the subtree balance or not and also save the calculated height of 
            above calculation

            3 conditions should satisfy:
            left_subtree balanced
            right_subtree balanced
            abs(left_height-right_height)<=1 (main tree balanced)

            to do this we return 2 things, balanced flag and current tree height
            """
            # if a empty tree then its balanced and we can mark the 
            # height as -1 so that single node will have height 1
            if not node:
                return True, -1
            left_balanced, left_height = balancedUtils(node.left)
            if not left_balanced:
                return False, left_height
            right_balanced, right_height = balancedUtils(node.right)
            if not right_balanced:
                return False, right_height
            # condition three check with stored heights
            if abs(left_height-right_height)<=1:
                return True, 1+max(left_height, right_height)
            else:
                return False, 1+max(left_height, right_height)
        return balancedUtils(root)[0]

        
