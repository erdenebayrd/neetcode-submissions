class Solution:
    def numDecodings(self, s: str) -> int:
        # time: O(N)
        # space: O(1)
        # method: DP
        if s[0] == '0':
            return 0

        n = len(s)
        prev_prev = 1
        prev = 1
        cur = 0
        for i in range(1, n):
            if s[i] != '0':
                cur = prev
            if 10 <= int(s[i - 1: i+1]) <= 26:
                cur += prev_prev
            prev_prev = prev
            prev = cur
        
        return cur