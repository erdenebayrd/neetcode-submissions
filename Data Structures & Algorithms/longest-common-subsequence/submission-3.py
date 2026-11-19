class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time: O(n * m) n len of text1, m is len of text2
        # space: O(m)
        # method: DP
        n = len(text1)
        m = len(text2)
        prev_row = [0] * m
        for i in range(m):
            if text1[0] == text2[i]:
                prev_row[i] = 1
            else:
                if i - 1 >= 0:
                    prev_row[i] = max(prev_row[i], prev_row[i - 1])

        result = max(prev_row)

        for i in range(1, n):
            row = [0] * m
            for j in range(m):
                if text1[i] == text2[j]:
                    row[j] += 1
                    if j - 1 >= 0:
                        row[j] += prev_row[j - 1]
                else:
                    row[j] = prev_row[j]
                    if j - 1 >= 0:
                        row[j] = max(row[j], row[j - 1])
            prev_row = row[:]
            result = max(result, max(prev_row))

        return result
        