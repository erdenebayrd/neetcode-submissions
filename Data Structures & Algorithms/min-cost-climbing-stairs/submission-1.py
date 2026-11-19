class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: DP
        inf = float('inf')
        n = len(cost)
        prev_prev = prev = 0
        cur = inf
        for i in range(2, n):
            cur = min(cur, prev_prev + cost[i - 2])
            cur = min(cur, prev + cost[i - 1])
            prev_prev = prev
            prev = cur
            cur = inf
        
        return min(prev + cost[-1], prev_prev + cost[-2])