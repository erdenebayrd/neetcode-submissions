from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def visit(row: int, col: int) -> int:
            result = 0
            queue = deque()
            queue.append((row, col))
            while queue:
                current_row, current_col = queue.popleft()
                result += 1
                # assert grid[current_row][current_col] == 1
                grid[current_row][current_col] = 0 # marked as visited
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_col = current_row + delta_row, current_col + delta_col
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] == 0:
                        continue
                    queue.append((next_row, next_col))
            return result


        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                result = max(result, visit(row, col))
        return result