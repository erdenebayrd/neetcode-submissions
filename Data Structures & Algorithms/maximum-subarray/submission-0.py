import heapq

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: O(n log n)
        # space: O(n)
        # method: heap
        n = len(nums)
        min_heap = [0]
        prefix = nums[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        result = float('-inf')
        for i in range(n):
            result = max(prefix[i] - min_heap[0], result)
            heapq.heappush(min_heap, prefix[i])
        return result