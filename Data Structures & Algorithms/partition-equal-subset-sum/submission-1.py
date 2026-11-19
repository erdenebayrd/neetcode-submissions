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

        @cache
        def can(index: int, amount: int) -> bool:
            if amount < 0:
                return False

            if index >= n:
                return amount == 0

            # take number at index
            result = can(index + 1, amount - nums[index])

            # not take number at index
            result |= can(index + 1, amount)
            
            return result
        
        return can(0, total // 2)