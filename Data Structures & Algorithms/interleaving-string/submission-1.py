from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time: O(len(s1) * len(s2) * len(s3))
        # space: O(len(s1) * len(s2) * len(s3))
        # method: DP top down

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def solve(i: int, j: int, flag: bool) -> bool:
            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            
            if (flag and i >= len(s1)) or (not flag and j >= len(s2)):
                return False
            
            if (flag and s1[i] != s3[i + j]) or (not flag and s2[j] != s3[i + j]):
                return False
            
            if flag:
                return solve(i + 1, j, True) or solve(i + 1, j, False)

            return solve(i, j + 1, True) or solve(i, j + 1, False)

        
        return solve(0, 0, True) or solve(0, 0, False)