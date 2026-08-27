class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def reachable(row: int, col: int, water: int) -> bool:
            if grid[row][col] > water:
                return False
            if row == n - 1 and col == n - 1:
                return True
            
            result = False
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or (next_row, next_col) in seen:
                    continue
                seen.add((next_row, next_col))
                result |= reachable(next_row, next_col, water)
            return result
        
        low, high = -1, n * n
        while low + 1 < high:
            mid = (low + high) // 2
            seen = set()
            seen.add((0, 0))
            if reachable(0, 0, mid):
                high = mid
            else:
                low = mid
        
        return high
            