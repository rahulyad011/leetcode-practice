class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_ind = -1
        max_ind = -1
        min_ele = 1000000
        max_ele = -1000000
        for i,num in enumerate(nums):
            if num >= max_ele:
                max_ele = num
                max_ind = i
            if num <= min_ele:
                min_ele = num
                min_ind = i
        
        n = len(nums)-1
        seperate_del = min(n-min_ind+1, min_ind+1) + min(n-max_ind+1, max_ind+1)
        combine_del = min(max(min_ind+1, max_ind+1), max(n-min_ind+1, n-max_ind+1))
        
        return min(seperate_del, combine_del)
            
        