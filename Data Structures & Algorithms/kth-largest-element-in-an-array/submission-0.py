import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for number in nums:
            heapq.heappush(largest, number)
            if len(largest) > k:
                heapq.heappop(largest)
        return largest[0]