class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        this is one of the most intelligent problem:
        for picking the majortiy element without using hashmap(O(n) runtime 
        and O(k) space), we can do simple counting with selecting one number
        as choice until others reduce the count to < 0, here we change the choice
        this way we will reach to a point where majority element will 
        prevail and led the count
        """
        choice = nums[0]
        count = 0
        for num in nums:
            if choice == num:
                count+=1
            else:
                count-=1
            if count < 0:
                choice = num
                count = 1
        return choice