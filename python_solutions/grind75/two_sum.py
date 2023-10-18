class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hint:
        # x + y = target => y = target - x
        # now if we find y in our dict we get the index
        # check for i!=j
        num_y = {}
        for i in range(len(nums)):
            num_y[target-nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in num_y and num_y[nums[j]] != j:
                return [j, num_y[nums[j]]]
        return -1