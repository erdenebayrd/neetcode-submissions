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
        dp = [[False] * n for _ in range(half + 1)]
        for i in range(n):
            dp[0][i] = True
        
        for amount in range(1, half + 1):
            for i in range(n):
                # take
                if amount - nums[i] >= 0 and i - 1 >= 0:
                    dp[amount][i] |= dp[amount - nums[i]][i - 1]

                # not take
                if i - 1 >= 0:
                    dp[amount][i] |= dp[amount][i - 1]
        
        return dp[half][n - 1]
