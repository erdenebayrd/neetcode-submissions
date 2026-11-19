from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n ^ 2) n is len of prices
        # space: O(n ^ 2)
        # method: DP
        n = len(prices)

        @cache
        def solve(last_bought_index: int, current_index: int) -> int:
            if current_index >= n:
                return 0
            
            result = 0
            if last_bought_index == -1: # nothing bought
                # buy
                result = max(result, solve(current_index, current_index + 1))
                
                # not buy
                result = max(result, solve(last_bought_index, current_index + 1))
            else:
                # sell
                result = max(result, solve(-1, current_index + 2) + prices[current_index] - prices[last_bought_index])

                # not sell
                result = max(result, solve(last_bought_index, current_index + 1))
            
            return result
        
        return solve(-1, 0)