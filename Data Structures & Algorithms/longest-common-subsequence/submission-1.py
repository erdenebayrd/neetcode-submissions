class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time: O(n * m) n len of text1, m is len of text2
        # space: O(m)
        # method: DP
        n = len(text1)
        m = len(text2)
        dp = [0] * m
        for i in range(m):
            if text1[0] == text2[i]:
                dp[i] = 1

        for i in range(1, n):
            row = [0] * m
            for j in range(m):
                if text1[i] == text2[j]:
                    row[j] += 1
                    if j - 1 >= 0:
                        row[j] += dp[j - 1]
                else:
                    row[j] = dp[j]
                    if j - 1 >= 0:
                        row[j] = max(row[j], row[j - 1])
            dp = row
        return dp[-1]