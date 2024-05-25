# https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        There will be three cases:
        mid == target -- return mid --simple case(lucky pick)

        else there are two cases for checking the sorted array possibility:
            if mid > left:  # left part of the pivoted array
                # check if present in the left sorted array
                if target is in between left and mid --> right = mid-1 (from here it will be a binary search)
                else not yet sorted so exclude --> left = mid+1
            else  # right part of the pivoted array
                # check if present in the right sorted array
                if target is in between mid and right --> left = mid+1 (from here it will be a binary search)
                else not yet sorted so exclude --> right = mid-1
        """
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            # check if left is sorted
            if nums[mid] >= nums[l]:
                if nums[mid] > target and nums[l]<=target:
                    r = mid-1
                else:
                    l = mid+1
            #check if right is sorted
            else:
                if nums[mid] < target and nums[r]>=target:
                    l = mid+1
                else:
                    r = mid-1

        return -1

