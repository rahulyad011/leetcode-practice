class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_item = max(nums)
        if max_item <= 0:
            return max_item
        l = 0
        r = 0
        sum_w = 0
        max_sum = 0
        for r in range(len(nums)):
            sum_w += nums[r]
            if sum_w <= 0:
                l=r+1
                sum_w = 0
                continue
            if sum_w > max_sum:
                max_sum = sum_w
        return max_sum