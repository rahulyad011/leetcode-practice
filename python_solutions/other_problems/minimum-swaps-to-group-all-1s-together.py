# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together

"""
Solution:
This is a intelligent sliding window solution.
It can be solved with fixed window technique
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #window size to form
        k = sum(data)
        if k==0 or k==1:
            return 0
        l=0
        r=k-2
        curr_sum = sum(data[l:k-1])
        max_sum = 0
        r+=1
        # get max sum for the fixed window size
        while r<len(data):
            curr_sum += data[r]
            if curr_sum>max_sum:
                max_sum = curr_sum
            curr_sum -= data[l]
            l+=1
            r+=1
        # k is the fixed windows size(total sum of zeroes)
        # max_sum is the ones that are already present in this window
        return k-max_sum