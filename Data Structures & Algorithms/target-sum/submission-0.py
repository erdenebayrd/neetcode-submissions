from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # time: O(n * sum(nums))
        # space: O(n * sum(nums))
        # DP top down

        total = 0
        for number in nums:
            total += abs(number)
        
        if not (-total <= target <= total):
            return 0
        
        n = len(nums)

        @cache
        def solve(index: int, target: int) -> int:
            if index >= n:
                if target == 0:
                    return 1
                return 0

            return solve(index + 1, target - nums[index]) + solve(index + 1, target + nums[index])
        
        return solve(0, target)
            