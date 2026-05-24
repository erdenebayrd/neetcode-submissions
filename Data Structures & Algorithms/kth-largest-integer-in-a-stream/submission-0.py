import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.values = []
        self.k = k
        for number in nums:
            heapq.heappush(self.values, number)
        
        while len(self.values) > k:
            heapq.heappop(self.values)

    def add(self, val: int) -> int:
        heapq.heappush(self.values, val)
        if len(self.values) > self.k:
            heapq.heappop(self.values)
        return self.values[0]