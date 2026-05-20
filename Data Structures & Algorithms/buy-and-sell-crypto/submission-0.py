class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        right_max = 0
        for i in range(n - 1, -1, -1):
            result = max(result, right_max - prices[i])
            right_max = max(prices[i], right_max)
        return result