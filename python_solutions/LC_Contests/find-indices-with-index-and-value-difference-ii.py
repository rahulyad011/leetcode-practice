# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_index = 0
        max_index = 0

        """
        Solution:
        this loop always keep the index difference >= indexDifference
        so first condition is matched
        now inside loop we check for valueDifference codition for which 
        we use min and max values
        as the value difference can be true in two cases if 
        |curr-min| > value_diff
        |curr-max| > value_diff
        we consider min and max difference only as it this is 
        not true then intermidate can never be true and we need to 
        return on possible answer not all
        """
        for i in range(indexDifference, n):

            # find min_index
            if nums[i-indexDifference] < nums[min_index]:
                min_index = i-indexDifference

            # find max_index
            if nums[i-indexDifference] > nums[max_index]:
                max_index= i-indexDifference

            # value diff comparision with min value(which is 
            #greater then indexdifference away from i)
            if abs(nums[i] - nums[min_index]) >= valueDifference:
                return [min_index, i]
            
            # value diff comparision with max value(which is 
            #greater then indexdifference away from i)
            if abs(nums[i] - nums[max_index]) >= valueDifference:
                return [max_index, i]
        return [-1, -1]