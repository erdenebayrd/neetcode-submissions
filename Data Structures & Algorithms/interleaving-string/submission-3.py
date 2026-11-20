from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time: O(len(s1) * len(s2))
        # space: O(len(s1) * len(s2))
        # method: DP top down

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def solve(i: int, j: int) -> bool:
            if i + j == len(s3):
                return True
            
            result = False
            if i < len(s1) and s1[i] == s3[i + j]:
                result |= solve(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                result |= solve(i, j + 1)
            return result

        
        return solve(0, 0)