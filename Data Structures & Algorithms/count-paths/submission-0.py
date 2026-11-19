class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time: O(n * m)
        # space: O(n)
        # method: DP

        """
            0 1 2 3 4 5
         0  1 1 1 1 1 1
         1  1 2 3 4 5 6 
         2  1 3 6 10 15 21
        """

        dp = [1] * n
        curr = 0
        for row in range(1, m):
            prev = 0
            for col in range(n):
                curr = prev + dp[col]
                prev = curr
                dp[col] = curr

        return curr