class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O(n * sum(nums))
        # space: O(sum(nums))
        # method: DP

        total = sum(nums)
        if total & 1:
            return False
        
        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True
        n = len(nums)
        
        for i in range(n):
            for total in range(1, half + 1):
                if total - nums[i] < 0:
                    continue
                dp[total] |= dp[total - nums[i]]

        return dp[half]