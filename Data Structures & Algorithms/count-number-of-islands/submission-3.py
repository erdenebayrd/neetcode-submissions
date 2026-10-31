from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: bfs

        seen = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    count += 1
                    queue = deque()
                    queue.append((row, col))
                    seen.add((row, col))
                    while queue:
                        current_row, current_col = queue.popleft()
                        for delta_row, delta_col in directions:
                            next_row, next_col = delta_row + current_row, delta_col + current_col
                            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] == "0" or (next_row, next_col) in seen:
                                continue
                            seen.add((next_row, next_col))
                            queue.append((next_row, next_col))

        return count