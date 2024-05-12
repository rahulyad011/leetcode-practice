"""
Tricky part here is how you manage the index for the solution1
actually we need to fix run to maximum len(nums)-p2 wher p2 is number of 2s.
This will avoid us form updating 2 again
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        solution2: Hashmap count of 0, 1, 2
        time : O(N), O(3)
        can we do better? i.e no extra space of hashing
        """
        # count_map = collections.Counter(nums)
        # ind = 0
        # ele = 0
        # while ind<len(nums):
        #     for i in range(count_map[ele]):
        #         nums[ind+i] = ele
        #     ind+=count_map[ele]
        #     ele+=1

        """
        solution1: swap and maintain two pointer for o and 2
        time : O(N), O(1)
        """
        # intial position of 0 and 2
        p0 = 0
        p2= len(nums)-1

        def swap(ind1, ind2):
            temp = nums[ind1]
            nums[ind1] = nums[ind2]
            nums[ind2] = temp

        i=0
        while i<=p2:
            if nums[i]==0:
                swap(p0, i)
                p0+=1
            elif nums[i]==2:
                swap(p2, i)
                p2-=1
                i-=1
            i+=1


