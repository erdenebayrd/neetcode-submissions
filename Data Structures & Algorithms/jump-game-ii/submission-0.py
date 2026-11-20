from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n) n is len of nums
        # method: BFS
        n = len(nums)
        queue = deque([(0, 0)]) # (index, steps taken)
        right_most = 0

        while queue:
            index, steps = queue.popleft()
            if index == n - 1:
                return steps
            left = right_most + 1
            right = min(n - 1, index + nums[index])
            for i in range(left, right + 1):
                queue.append((i, steps + 1))
            
            right_most = max(right_most, right)
        
        return -1