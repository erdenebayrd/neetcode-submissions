from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: multisource BFS
        rows = len(grid)
        cols = len(grid[0])

        inf = float('inf')
        dist = [[inf] * cols for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2: # rotten fruit
                    queue.append((row, col))
                    dist[row][col] = 0
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] != 1:
                    continue
                if dist[next_row][next_col] > dist[row][col] + 1:
                    dist[next_row][next_col] = dist[row][col] + 1
                    queue.append((next_row, next_col))
        
        result = -inf
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result = max(result, dist[row][col])
        
        if result == -inf or result == inf:
            result = -1
        return result