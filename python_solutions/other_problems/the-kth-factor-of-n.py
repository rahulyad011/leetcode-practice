# https://leetcode.com/problems/the-kth-factor-of-n


from heapq import heapify, heappush, heappop

"""
This problem is derived from a beautiful maths concept that if
if a if the divisor of n the quotient b is also the divisor
b=n//a
so we need to effective just check till the sqrt(n) and add all the divisor and the respective quotient

the second solution the one with maths is on the same idea just return if kth comes into the other divisor(b). We need to find the first divisor and then divide n by that to get kth.
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        """Heap Solution"""
        """checking till sqrt(n)"""
        if n==0:
            return 0
        factor = int(math.sqrt(n))
        heap = []
        heapify(heap)
        while factor:
            if n%factor==0:
                heappush(heap, -factor)
                second = n//factor
                if second != factor:
                    heappush(heap, -second)
            factor-=1
            while len(heap) > k:
                heappop(heap)
        if len(heap) < k:
            return -1
        return -heap[0]


        """Without heap optimal solution"""
        """checking till sqrt(n)"""
        # if n==0:
        #     return 0
        # sqrt_n = int(math.sqrt(n))
        # divisors=[]
        # for i in range(1, sqrt_n+1):
        #     first = i
        #     if n%first == 0:
        #         # second = n//first
        #         divisors.append(first)
        #         # if first!=second:
        #         #     divisors.append(second)
        #         k-=1
        #         if k==0:
        #             return first
        # if sqrt_n*sqrt_n==n:
        #     k+=1
        # if len(divisors) < k:
        #     return -1
        # else:
        #     return n//divisors[len(divisors)-k]


