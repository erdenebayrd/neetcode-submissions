from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP

        if s[0] == '0':
            return 0

        n = len(s)

        @cache
        def solve(index: int) -> int:
            if index >= n:
                return 1
            
            if s[index] == '0':
                return 0

            result = solve(index + 1)
            if index + 1 < n and int(s[index:index+2]) <= 26:
                result += solve(index + 2)
            return result
        
        result = solve(1)
        if n >= 2 and int(s[:2]) <= 26:
            result += solve(2)
        
        return result
