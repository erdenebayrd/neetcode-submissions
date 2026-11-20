class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time: O(n) n is len of nums array
        # space: O(1) 
        # method: BFS
        
        n = len(nums)
        right = 0
        index = 0

        while index <= right:
            right = max(right, index + nums[index])
            right = min(right, n - 1)
            index += 1
        
        return right == n - 1