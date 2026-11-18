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
        if self.is_connected(node_u, node_v):
            return
        parent_u = self.find_parent(node_u)
        parent_v = self.find_parent(node_v)
        if parent_u not in self.rank:
            self.rank[parent_u] = 0
        if parent_v not in self.rank:
            self.rank[parent_v] = 0
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else: # same rank
            self.rank[parent_u] += 1
            self.parent[parent_v] = parent_u

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # time: O(N ^ 2 * log (N ^ 2))
        # space: O(N)
        # method: Kruskal
        
        def dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(points[i], points[j]), i, j))
        
        edges.sort()
        cost = 0
        dsu = DSU()
        for weight, i, j in edges:
            if not dsu.is_connected(i, j):
                cost += weight
                dsu.connect(i, j)
        return cost