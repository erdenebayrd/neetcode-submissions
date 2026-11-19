from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n) n is len of prices
        # space: O(n)
        # method: DP
        n = len(prices)

        @cache
        def solve(index: int, bought: bool) -> int:
            if index >= n:
                return 0
            result = solve(index + 1, bought)
            if bought:
                result = max(result, solve(index + 2, False) + prices[index])
            else:
                result = max(result, solve(index + 1, True) - prices[index])
            return result
        
        return solve(0, False)