from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: multisource BFS in opposite dir edges
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]        
        graph = {"pacific": set(), "atlantic": set()}

        for row in range(rows):
            graph["pacific"].add((row, 0))
            graph["atlantic"].add((row, cols - 1))
        
        for col in range(cols):
            graph["pacific"].add((0, col))
            graph["atlantic"].add((rows - 1, col))
        
        visited = {}
        for row in range(rows):
            for col in range(cols):
                visited[(row, col)] = 0
                graph[(row, col)] = set()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or heights[row][col] > heights[next_row][next_col]:
                        continue
                    graph[(row, col)].add((next_row, next_col))
        
        def bfs(source, flag) -> None:
            queue = deque()
            queue.append(source)
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] & flag:
                        continue
                    queue.append(neighbor)
                    visited[neighbor] ^= flag

        result = []
        bfs("pacific", 1)
        bfs("atlantic", 2)
        for row, col in visited:
            if visited[(row, col)] == 3:
                result.append([row, col])
        
        return result