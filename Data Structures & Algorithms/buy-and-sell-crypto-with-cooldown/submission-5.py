class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n) n is len of prices
        # space: O(1)
        # method: DP bottom up
        n = len(prices)
        if n <= 1:
            return 0
        
        # dp = [[0] * 2 for _ in range(n)]
        
        # dp[0][0] = -prices[0]
        # dp[1][0] = max(dp[0][0], -prices[1])
        # dp[0][1] = 0
        # dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])

        # for i in range(2, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        # return max(dp[n - 1])
        prev_prev_bought = -prices[0]
        prev_prev_sold = 0
        prev_bought = max(prev_prev_bought, -prices[1])
        prev_sold = max(prev_prev_sold, prev_prev_bought + prices[1])
        for i in range(2, n):
            cur_bought = max(prev_bought, prev_prev_sold - prices[i])
            cur_sold = max(prev_sold, prev_bought + prices[i])
            prev_prev_bought = prev_bought
            prev_prev_sold = prev_sold
            prev_bought = cur_bought
            prev_sold = cur_sold

        return max(prev_bought, prev_sold)