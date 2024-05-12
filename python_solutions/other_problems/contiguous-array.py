# https://leetcode.com/problems/contiguous-array/

"""
Solution:
this a important application problem of hashmap
Add 1 to total sum is number is 1
else add -1 to total sum if the number is 0
hashmap saves the index of all the sums.
Now if a sum reappears then that means there we have equal number of zeroes and ones as that contribute to zero sum
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summap = {}
        max_length = 0
        total = 0
        summap[0] = -1
        for i, num in enumerate(nums):
            if num==0:
                total-=1
            else:
                total+=1
            if total not in summap:
                summap[total] = i
            else:
                max_length = max(max_length, i-summap[total])
        return max_length
