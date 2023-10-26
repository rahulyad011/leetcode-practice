class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Solution : Thought the middle will give the final insert result in 
        all scerios but actually as the loop is going until l<=r so l is 
        updated according to the final value of middle and thats why l gives 
        the final index where target can be inserted"""
        l = 0
        r = len(nums)-1
        middle = 0
        while l<=r:
            middle = l + (r-l)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle+1
            else:
                r = middle - 1
        return l
        
        