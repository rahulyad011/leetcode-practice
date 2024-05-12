"""
solution: simple idea of this oslution is that one of the part will be sorted 
whenever we pick a random index in the array, due to this property we will be able 
to compare the target every time and move mid accoringly
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                return mid
            #check is left array is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                #check if right array is sorted
                if nums[r] >= target > nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return -1    
        
        
                