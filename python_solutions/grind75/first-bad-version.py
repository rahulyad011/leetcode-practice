# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

     """
     Learning:
        this is similar to binary search problem as we need to 
        find the pivot element, just change is how to maintain the mid pointer 
        if there is a bad version found
        use this pattern only when using binary search(this is full proof)
    """
    def binary_search(self, start, end):
        mid = start + int((end-start)/2)
        if start == end:
            if isBadVersion(start):
                return start
        if not isBadVersion(mid):
            return self.binary_search(mid+1, end)
        else:
            return self.binary_search(start, mid)


    def firstBadVersion(self, n: int) -> int:
        return self.binary_search(1, n)

    """
    Solution: Iterative
    """

    # def firstBadVersion(self, n: int) -> int:
    #     """variation of binary search"""
    #     l = 1
    #     r = n
    #     mid = 1
    #     while l<=r:
    #         mid = l + ((r-l)//2)
    #         if isBadVersion(mid):
    #             r = mid-1
    #         else:
    #             l = mid+1
    #     if isBadVersion(mid):
    #         return mid
    #     if isBadVersion(mid+1):
    #         return mid+1
        