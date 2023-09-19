class KthLargest:
    """
        learning1:
        kth largest means the smallest of top k elements that means 
        this needs to be solved with min heap
    """
    heap = []
    size = 0
    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.size:
            heappop(self.heap)
        # print("initial heap", self.heap)

    def add(self, val: int) -> int:
        if len(self.heap)==self.size:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        # print("heap", self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)