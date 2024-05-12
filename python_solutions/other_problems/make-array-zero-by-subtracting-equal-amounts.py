# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        "Set Solution: Fast"
        unique = set(nums)
        if 0 in unique:
            return len(unique)-1
        else:
            return len(unique)

        "Without Sorting: get min: slowest O(N2)"
        # n = len(nums)
        
        # count = 0
        # while nums != [0]*n:
        #     count += 1
        #     small = min([i for i in nums if i > 0])
        #     for i in range(n):
        #         if nums[i] != 0:
        #             nums[i] -= small
        # return count

        "Sorting solution: slow"
        # nums.sort()
        # curr_index = 0
        # ops = 0
        # while curr_index<len(nums):
        #     if nums[curr_index]==0:
        #         curr_index+=1
        #     else:
        #         temp = nums[curr_index]
        #         for i in range(curr_index, len(nums)):
        #             nums[i] = nums[i]-temp
        #         ops+=1
        # return ops