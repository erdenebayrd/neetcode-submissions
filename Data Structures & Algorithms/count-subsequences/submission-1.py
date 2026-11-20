from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # time: O(n * m) n is len of s, m is len of t
        # space: O(n * m)
        # method: DP top down
        n, m = len(s), len(t)

        @cache
        def count(i: int, j: int) -> int:
            if j == m:
                return 1
            if i >= n:
                return 0
            
            result = count(i + 1, j)
            if s[i] == t[j]:
                result += count(i + 1, j + 1)
            return result
        
        return count(0, 0)