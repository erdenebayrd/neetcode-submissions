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
                if p[j] != '*':
                    return False
                
                return is_match(i, j + 1)
            
            if s[i] == p[j] or p[j] == '.':
                return is_match(i + 1, j + 1)
            
            if p[j] == '*':
                prev_char = p[j - 1]
                if prev_char == '.' or prev_char == s[i]:
                    return is_match(i + 1, j) or is_match(i + 1, j + 1)
            
            return False
        
        return is_match(0, 0)