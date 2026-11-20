import heapq

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: O(n log n)
        # space: O(n)
        # method: prefix sum
        n = len(nums)
        prefix = nums[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        current_min = 0
        
        result = float('-inf')
        for i in range(n):
            result = max(prefix[i] - current_min, result)
            current_min = min(current_min, prefix[i])

        return result