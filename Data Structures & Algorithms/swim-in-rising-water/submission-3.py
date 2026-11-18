class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find_parent(self, node):
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def is_connected(self, node_u, node_v):
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        return parent_u == parent_v
    
    def connect(self, node_u, node_v):
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        if parent_u == parent_v:
            return
        if parent_u not in self.rank:
            self.rank[parent_u] = 0
        if parent_v not in self.rank:
            self.rank[parent_v] = 0
        if self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        elif self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        else:
            self.rank[parent_v] += 1
            self.parent[parent_u] = parent_v

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # # time: O(N ^ 2 log N)
        # # space: O(N ^ 2)
        # # method: Dijkstra

        # min_heap = [(grid[0][0], 0, 0)]
        # result = grid[0][0]
        # seen = set([(0, 0)])
        # directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # rows = len(grid)
        # cols = len(grid[0])

        # while min_heap:
        #     height, row, col = heapq.heappop(min_heap)
        #     result = max(result, height)
        #     if row == rows - 1 and col == cols - 1:
        #         break
        #     for delta_row, delta_col in directions:
        #         next_row, next_col = row + delta_row, col + delta_col
        #         if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in seen:
        #             continue
        #         heapq.heappush(min_heap, (grid[next_row][next_col], next_row, next_col))
        #         seen.add((next_row, next_col))
                
        # return result


        """
        since the grid value never exceeds n ^ 2
        we can connect nodes at each time  step at t if their values are lower or equal to t using DSU
        then check source and target nodes are connected or not.
        the first t would be answer when source and target nodes are connected component.
        """
        # time: O(N ^ 2 * Ackerman(N ^ 2)) Ackerman(N ^ 2) is almost constant
        # space: O(N ^ 2)
        # method: DSU + greedy
        rows = len(grid)
        cols = len(grid[0])
        source = (0, 0)
        target = (rows - 1, cols - 1)
        values = {}
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] not in values:
                    values[grid[row][col]] = []
                values[grid[row][col]].append((row, col))

        dsu = DSU()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for timestamp in range(rows * cols):
            if timestamp not in values:
                continue
            for row, col in values[timestamp]:
                for delta_row, delta_col in directions:
                    neighbor_row, neighbor_col = row + delta_row, col + delta_col
                    if neighbor_row < 0 or neighbor_row >= rows or neighbor_col < 0 or neighbor_col >= cols or grid[neighbor_row][neighbor_col] > timestamp:
                        continue
                    dsu.connect((row, col), (neighbor_row, neighbor_col))
            if dsu.is_connected(source, target):
                return timestamp
        
        return rows * cols