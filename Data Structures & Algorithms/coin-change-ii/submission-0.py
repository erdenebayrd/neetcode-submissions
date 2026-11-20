from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # time: O(n * amount)
        # space: O(n * amount)
        # method: DP top down
        n = len(coins)

        @cache
        def solve(index: int, amount: int) -> int:
            if amount == 0:
                return 1
            if amount < 0 or index >= n:
                return 0
            
            # take
            result = solve(index, amount - coins[index])

            # skip
            result += solve(index + 1, amount)

            return result
        
        return solve(0, amount)