from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O(n * sum(nums))
        # space: O(sum(nums) * n)
        # method: DP

        total = sum(nums)
        if total & 1:
            return False
        
        n = len(nums)
        half = total // 2
        amounts = [False] * (half + 1)
        amounts[0] = True

        for number in nums:
            for amount in range(half, number - 1, -1):
                amounts[amount] |= amounts[amount - number]
        
        return amounts[half]