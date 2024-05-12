# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

"""Solution:
This is a combination of the two sliding window problems:
1. subarray without duplicate
2. subarray with a fixed window
The key part is how we move the left pointer and curr_sum when duplicate found
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        character_map = {}
        max_sum = 0
        curr_sum = 0
        for r in range(len(nums)):
            if nums[r] in character_map:
                if character_map[nums[r]] >= l:
                    l = character_map[nums[r]]+1
                    curr_sum = sum(nums[l:r])
            curr_sum += nums[r]
            character_map[nums[r]] = r
            if r-l+1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum-= nums[l]
                l+=1
        return max_sum
            
        