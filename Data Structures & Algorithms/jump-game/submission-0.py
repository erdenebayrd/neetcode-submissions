from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time: O(n)
        # space: O(n) n is len of nums array
        # method: BFS
        
        n = len(nums)
        queue = deque([0])
        right_index = 0

        while queue:
            index = queue.popleft()
            if index == n - 1:
                return True

            left = right_index + 1
            right = min(n - 1, index + nums[index])
            for i in range(left, right + 1):
                queue.append(i)

            right_index = max(right_index, right)

        return False