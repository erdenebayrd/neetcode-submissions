import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # time: O(N ^ 2 log N)
        # space: O(N ^ 2)
        # method: Dijkstra

        min_heap = [(grid[0][0], 0, 0)]
        result = grid[0][0]
        seen = set([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        while min_heap:
            height, row, col = heapq.heappop(min_heap)
            result = max(result, height)
            if row == rows - 1 and col == cols - 1:
                break
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in seen:
                    continue
                heapq.heappush(min_heap, (grid[next_row][next_col], next_row, next_col))
                seen.add((next_row, next_col))
                
        return result