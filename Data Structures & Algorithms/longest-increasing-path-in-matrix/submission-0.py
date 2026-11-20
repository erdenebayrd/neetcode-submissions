from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DP top down
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        @cache
        def lis(row: int, col: int) -> int:
            longest = 1
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                
                if matrix[row][col] < matrix[next_row][next_col]:
                    longest = max(longest, 1 + lis(next_row, next_col))
            
            return longest
        
        longest = 0
        for row in range(rows):
            for col in range(cols):
                longest = max(longest, lis(row, col))
        
        return longest