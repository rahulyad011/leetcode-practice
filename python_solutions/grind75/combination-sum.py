# https://leetcode.com/problems/combination-sum/

"""
Solution:
This is a good problem of recursion with back tracking
Similar to coin change(with unlimited coin) here we have two options.
1. take the candidate and results the target sum
2. no to take the candidate
But the trick is that we need to return the possiblecombinations not just true and false.
So this is the reason we keep two arrays results(master), currarr(curr itereation combinations)
first we include the element(append) and try to form combination and then we backtrack and remove the element(pop) and find other combinations without usin it
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combUtils(numbers, aim, n, curr_arr):
            if aim==0:
                result.append(curr_arr.copy())
                return 
            if n==0:
                return
            if numbers[n-1]>aim:
                combUtils(numbers, aim, n-1, curr_arr)
            else:
                curr_arr.append(numbers[n-1])
                combUtils(numbers, aim-numbers[n-1], n, curr_arr)
                curr_arr.pop()
                combUtils(numbers, aim, n-1, curr_arr)
        combUtils(candidates, target, len(candidates), [])
        return result
