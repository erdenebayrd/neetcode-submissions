from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        result = []
        
        for i in range(k, len(nums)):
            index = queue[0]
            result.append(nums[index])
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            while queue and queue[0] <= i - k:
                queue.popleft()
        result.append(nums[queue[0]])
        queue.clear()
        return result