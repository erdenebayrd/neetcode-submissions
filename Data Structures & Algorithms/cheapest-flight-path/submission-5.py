from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # time: O(K * V + E)
        # space: O(V + E)
        # method: Bellmon-Ford
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        queue = deque()
        queue.append((src, dist[src], 0))
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))

        while queue:
            node, current_dist, stops = queue.popleft()
            if stops > k:
                continue
            for neighbor, weight in graph[node]:
                if current_dist + weight < dist[neighbor]:
                    dist[neighbor] = current_dist + weight
                    queue.append((neighbor, dist[neighbor], stops + 1))
        
        if dist[dst] == inf:
            return -1
        return dist[dst]