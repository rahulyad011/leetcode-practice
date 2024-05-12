# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements

from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # def swap(index1, index2):
        #     temp = nums[index1]
        #     nums[index1]= nums[index2]
        #     nums[index2] = temp
        
        # swap_possible = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]>nums[j] and (nums[i]-nums[j]) <= limit:
        #             swap_possible.append((i, j))
        
        # while swap_possible:
        #     first, second = swap_possible.pop()
        #     swap(first, second)
        
        """Solution: Index Grouping
        After sorting We need to find groups of number having difference within the limit because
        for example: swaps 6 -> 4 and 4->2 then ultimately 2, 4, 6 thats means 2,6 can swap places not directly 
        but using 4 as pivot. So we just need to indentify the disjoint sets and then these sets 
        can be returned in a sorted manner
        As we can't change the orginal order so we need to sort keeping the original index intact for reference
        """
        n = len(nums)
        
        sorted_nums = sorted(nums)
        sorted_groups = [deque([sorted_nums[0]])]
        
        for i in range(1, n):
            if sorted_nums[i] - sorted_groups[-1][-1] <= limit:
                sorted_groups[-1].append(sorted_nums[i])
            else:
                sorted_groups.append(deque([sorted_nums[i]]))
        
        d = {}
        for i, sorted_group in enumerate(sorted_groups):
            for num in sorted_group:
                d[num] = i
        
        result = []
        for num in nums:
            result.append(sorted_groups[d[num]].popleft())
        return result