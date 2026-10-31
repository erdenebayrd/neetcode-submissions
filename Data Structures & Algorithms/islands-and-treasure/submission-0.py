from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: BFS
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] <= 0:
                    continue
                if grid[next_row][next_col] > grid[row][col] + 1:
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))
        