from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # time: O(K * V + E)
        # space: O(V)
        # method: Bellmon-Ford
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        queue = deque([src])
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))

        for _ in range(k + 1):
            next_queue = deque()
            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    if dist[neighbor] > dist[node] + weight:
                        next_queue.append(neighbor)
                        dist[neighbor] = dist[node] + weight
            queue = next_queue
        
        if dist[dst] == inf:
            return -1
        return dist[dst]