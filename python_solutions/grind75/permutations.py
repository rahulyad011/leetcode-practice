# https://leetcode.com/problems/permutations/

"""
Solution:
This is a classic problem of backtracing, not easy to get until we visualize it as a tree
Check the editorial section for the diagram: https://leetcode.com/problems/permutations/editorial/

So now the idea is to use backtracking and cover all the possibilties starting with [] arr then adding 1 element from the nums and then making it 2 elements and so on. Once the currarr size is equal to the size of the input arr, this is the permuation that we can add into the result
As you can visualize all the leaf nodes have the unique permuations as number of permuations are n!
so when reach a leaf node and add it in the result, we pop the element from currarr(backtracking) and then reach to the previous node and check for possibilties.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_arr = []
        def permuteUtil(curr_arr):
            if len(curr_arr) == len(nums):
                result.append(curr_arr.copy())
                return
            for num in nums:
                if num not in curr_arr:
                    curr_arr.append(num)
                    permuteUtil(curr_arr)
                    curr_arr.pop()
        permuteUtil([])
        return result
        
