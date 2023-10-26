class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1]*len(nums)
        if k == 0:
            return nums
        if k >= len(nums):
            return result
        window = 2*k+1
        # avg = int(sum(nums[0:window])/(window))
        avg = sum(nums[0:window])
        if 2*k+1 <= len(nums):
            result[k]=int(avg/window)
        for i in range(k+1, len(nums)-k):
            avg = avg - nums[i-k-1] + nums[i+k]
            result[i] = int(avg/window)
        return result