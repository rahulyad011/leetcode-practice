class Solution:
    start = 0

    ## learning1: if not using return in recursive calls then we need to save the result else None will bne returned
    ## learning2: index of mid element needs to be handled properly if modifying the original array as mid = start + mid
    """The issue with this code is that you are missing the return statements in the recursive calls. Since you are not returning anything from those recursive calls, the function will return None, leading to the "TypeError: None is not a valid value for the expected return type integer."""

    def search(self, nums: List[int], target: int) -> int:
        """
        iterative solution: using two pointers (l,r) and mid
        This can lead to overflow if l and r are large integers
        better would be used mid = l + (r-l)//2
        """
        l = 0
        r = len(nums)-1
        mid = 0
        if not nums:
            return -1
        while l <= r:
            mid = int((l + r)//2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1

        """
        recursive solution1: similar to the iterativ solution
        (two pointer start and end), just instead of while loop we 
        call recusion
        """
        # def binary_search(nums, target, start, end):
        #     if start>end or start>len(nums) or end<0:
        #         return -1
        #     else:
        #         mid = int(start + (end-start)//2)
        #         if target == nums[mid]:
        #             return mid
        #         elif target > nums[mid]:
        #             return binary_search(nums, target, mid+1, end)
        #         else:
        #             return binary_search(nums, target, start, mid-1)
        # return binary_search(nums, target, 0, len(nums)-1)

        
        """
        recrusive solution2: not using two pointers(start and end) 
        so need to reduce the list size as per
        the middle element comparision
        """
        # mid = int(len(nums)/2)
        
        # print(self.start, mid, nums)
        # mid_element = nums[mid]

        # if target == mid_element:
        #     return self.start + mid
        
        # if len(nums) <= 1:
        #     return -1

        # if target > mid_element:
        #     self.start += mid
        #     return self.search(nums[mid:], target)
        # elif target < mid_element:
        #     return self.search(nums[0:mid], target)
