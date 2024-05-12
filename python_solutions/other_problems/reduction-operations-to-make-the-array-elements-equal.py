# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal

# from heapq import heapify, heappop, heappush
# from collections import Counter, OrderedDict

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """solution1: sorting and then count 
        all the uniques and the keep the count of previous 
        saved until we reach minimum, this way count keeps on 
        increase with the number are reduced one by one
        for [10, 9, 8, 6, 5] -- here 10 will be counter in 9, 8 and 6 
        so keeping the previous count is important
        """
        nums.sort(reverse=True)
        # print(nums)
        count_ops=0
        # min_key = min(nums)
        previous = 0
        curr_value = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[len(nums)-1]:
                break
            if nums[i]!=nums[i+1]:
                count_ops += (previous+1)
            previous+=1
        return count_ops

        """solution2: sorting, counter"""
        # # count_map = {}
        # # for num in nums:
        # #     count_map[num] = count_map.get(num, 0) + 1
        # count_map = Counter(nums)
        # count_map = sorted(count_map.items(), key=lambda x: x[0], reverse=True)
        # # print(count_map)
        # count_ops=0
        # min_key = min(nums)
        # previous = 0
        # for key, value in count_map:
        #     if key == min_key:
        #         break
        #     # print(key, value, previous)
        #     count_ops+=(value+previous)
        #     previous += value
        # return count_ops


        """solution2: heap"""
        # count_map = Counter(nums)
        # min_element = min(nums)
        # heap = [-num for num in count_map.keys()]
        # # print("heap:", heap)
        # # creating heap
        # heapify(heap)
        # # top two largest element
        # first = heap[0]
        # second = 0
        # count_operations = 0
        # # print("heap:", heap)
        # while -first != min_element and len(heap):
        #     first = heappop(heap)
        #     if len(heap):
        #         second = heap[0]
        #     else:
        #         break
        #     # print("heap:", heap)
        #     # print("two numbers:", first, second)
        #     count_operations += count_map[-first]
        #     count_map[-second]+=count_map[-first]
        # return count_operations

        