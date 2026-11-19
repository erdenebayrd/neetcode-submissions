class Solution:
    def numDecodings(self, s: str) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1: i+1]) <= 26:
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
        return dp[n - 1]