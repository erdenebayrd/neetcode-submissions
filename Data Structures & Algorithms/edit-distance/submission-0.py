from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # time: O(n * m) n len of word1, m is len of word2
        # space: O(n * m)
        # method: DP top down

        n, m = len(word1), len(word2)

        @cache
        def calc(i: int, j: int) -> int:
            if j == m:
                return n - i # deleting cost
            
            if i >= n:
                return m - j # inserting chars at the end of word1 to make it equal to word2

            # delete char at i from word1
            result = 1 + calc(i + 1, j)

            # change char at i from word1 to make it equal to char at j of word2
            result = min(result, 1 + calc(i + 1, j + 1))

            # insert before char at i
            result = min(result, 1 + calc(i, j + 1))

            if word1[i] == word2[j]:
                result = min(result, calc(i + 1, j + 1))
            return result
        
        return calc(0, 0)