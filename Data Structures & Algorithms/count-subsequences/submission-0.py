class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            Input: s = "caaat", t = "cat"
               c a a a t
            c  1 1 1 1 1       
            a  0 1 2 3 3  
            t  0 0 0 0 3

            dp[i][j] = dp[i][j - 1]
            if s[j] == t[i]:
                dp[i][j] += dp[i - 1][j - 1]
            
        """
        # time: O(n * m) n len(s), m is len(t)
        # space: O(n)
        # method: DP bottom up
        n = len(s)
        m = len(t)
        prev_row = [1] * n
        
        for i in range(m):
            prev_col = 0
            curr_row = [0] * n
            for j in range(n):
                curr_row[j] += prev_col
                if t[i] == s[j]:
                    curr_row[j] += prev_row[j - 1]
                prev_col = curr_row[j]

            prev_row = curr_row
        
        return prev_row[-1]

