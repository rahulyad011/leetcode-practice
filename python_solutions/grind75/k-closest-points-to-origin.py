from heapq import heapify, heappush, heappop
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Solution: a classic heap proble, here we will maintain a k size max heap, so that kth element 
        is the max on the top of heap, if there is any coming element that is smaller than this top it
        will replace the top from the kcloset element of the heap"""
        heap = []
        heapify(heap)
        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            if len(heap)<k:
                heappush(heap, [-distance, point])
            else:
                if distance < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, [-distance, point])
        for i, item in enumerate(list(heap)):
            heap[i]=item[1]
        return heap