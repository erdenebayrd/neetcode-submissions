class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time: O(n * m) n len of text1, m is len of text2
        # space: O(n * m)
        # method: DP
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] += 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] += dp[i - 1][j - 1]
                else:
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if j - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[n - 1][m - 1]