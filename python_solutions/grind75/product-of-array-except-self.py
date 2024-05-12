# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """with extra memeory prefix and suffix array"""
        # prefix = [1]*len(nums)
        # suffix = [1]*len(nums)

        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i-1]*nums[i-1]

        # for i in range(len(nums)-2, -1, -1):
        #     suffix[i] = suffix[i+1]*nums[i+1]
        
        # for i in range(len(nums)):
        #     prefix[i] = prefix[i]*suffix[i]

        # return prefix

        output = [1]*len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]

        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix*nums[i+1]
            output[i] = output[i]*suffix
        
        return output

