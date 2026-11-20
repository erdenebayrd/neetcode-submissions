from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time: O(len(s1) * len(s2) * len(s3))
        # space: O(len(s1) * len(s2) * len(s3))
        # method: DP top down

        @cache
        def solve(i: int, j: int, k: int, flag: bool) -> bool:
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if k >= len(s3) or (flag and i >= len(s1)) or (not flag and j >= len(s2)):
                return False
            
            if (flag and s1[i] != s3[k]) or (not flag and s2[j] != s3[k]):
                return False
            
            if flag:
                return solve(i + 1, j, k + 1, True) or solve(i + 1, j, k + 1, False)

            return solve(i, j + 1, k + 1, True) or solve(i, j + 1, k + 1, False)

        
        return solve(0, 0, 0, True) or solve(0, 0, 0, False)