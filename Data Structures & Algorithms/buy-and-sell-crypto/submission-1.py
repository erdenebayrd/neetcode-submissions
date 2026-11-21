class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        cur_min = float('inf')
        for price in prices:
            result = max(result, price - cur_min)
            cur_min = min(cur_min, price)
        return result