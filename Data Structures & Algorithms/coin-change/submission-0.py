class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # time: O(n * amount) n is number diff coins
        # space: O(amount)
        # method: DP bottom up
        inf = float('inf')
        n = len(coins)
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin > current_amount:
                    continue
                dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - coin])
        
        if dp[amount] == inf:
            return -1
        
        return dp[amount]