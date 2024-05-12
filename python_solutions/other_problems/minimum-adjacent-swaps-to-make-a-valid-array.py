# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_element = (pow(10, 5)+1, -1)
        max_element = (0, -1)
        n = len(nums)
        for i in range(n):
            if nums[i] < min_element[0]:
                min_element = (nums[i], i)
            if nums[n-i-1] > max_element[0]:
                max_element = (nums[n-i-1], n-i-1)
        # print(min_element, max_element)
        swap_counts = (min_element[1]) + (n-1-max_element[1])
        if min_element[1] > max_element[1]:
            swap_counts -= 1
        return swap_counts