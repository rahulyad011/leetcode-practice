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