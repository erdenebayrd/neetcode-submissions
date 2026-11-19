class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n) n is len of prices
        # space: O(n)
        # method: DP bottom up
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            if i - 2 >= 0:
                dp[i][0] = max(dp[i][0], dp[i - 2][1] - prices[i])
            
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        return max(dp[n - 1])