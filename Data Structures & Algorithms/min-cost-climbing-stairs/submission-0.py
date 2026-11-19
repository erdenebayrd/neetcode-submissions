class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP
        inf = float('inf')
        n = len(cost)
        dp = [inf] * n
        dp[0] = dp[1] = 0
        for i in range(2, n):
            dp[i] = min(dp[i], dp[i - 1] + cost[i - 1])
            dp[i] = min(dp[i], dp[i - 2] + cost[i - 2])
        
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])