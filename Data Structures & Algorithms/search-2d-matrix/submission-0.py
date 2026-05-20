import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if target < matrix[0][0] or matrix[rows - 1][cols - 1] < target:
            return False
        
        low, high = -1, rows
        while low + 1 < high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target:
                low = mid
            else: # matrix[mid][0] > target
                high = mid
        col = bisect.bisect_left(matrix[low], target)
        return col < cols and matrix[low][col] == target