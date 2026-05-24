from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        def visit(row: int, col: int) -> None:
            queue = deque()
            queue.append((row, col))
            grid[row][col] = '0'
            while queue:
                current_row, current_col = queue.popleft()
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_col = current_row + delta_row, current_col + delta_col
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] == '0':
                        continue
                    grid[next_row][next_col] = '0'
                    queue.append((next_row, next_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0': # water or visited
                    continue
                result += 1
                visit(row, col)
        return result