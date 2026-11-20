from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        # time: O(n) n is len of nums
        # space: O(1) 
        # method: greedy
        n = len(nums)
        interval = [0, 0, 0] # left, right, steps taken
        while interval[1] < n - 1:
            left, right, steps = interval
            next_interval = [right + 1, right, steps + 1]
            for i in range(left, right + 1):
                next_interval[1] = max(next_interval[1], i + nums[i])
            interval = next_interval
            
        return interval[-1]