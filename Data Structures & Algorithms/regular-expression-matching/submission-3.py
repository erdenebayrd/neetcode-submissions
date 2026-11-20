from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # time: O(n * m) n is len of s, m is len of p
        # space: O(n * m)
        # method: DP top down
        n, m = len(s), len(p)

        @cache
        def is_match(i: int, j: int) -> bool:
            if i == n and j == m:
                return True
            
            if j >= m:
                return False
            
            if i >= n:
                if j + 1 < m and p[j + 1] == '*':
                    return is_match(i, j + 2)
                return False

            result = False
            if j + 1 < m and p[j + 1] == '*':
                result |= is_match(i, j + 2)
                if s[i] == p[j] or p[j] == '.':
                    result |= is_match(i + 1, j)
            else:
                if s[i] == p[j] or p[j] == '.':
                    result |= is_match(i + 1, j + 1)
            return result
        
        return is_match(0, 0)
                
