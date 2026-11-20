from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # time: O(n ^ 3)
        # space: O(n ^ 2)
        # method: DP top down
        n = len(nums)

        @cache
        def solve(left: int, right: int) -> int:
            if left + 1 >= right:
                return 0
            
            result = 0
            for i in range(left + 1, right):
                coins = nums[i]
                if 0 <= left < n:
                    coins *= nums[left]
                if 0 <= right < n:
                    coins *= nums[right]
                result = max(result, coins + solve(left, i) + solve(i, right))
            return result
            
        return solve(-1, n)