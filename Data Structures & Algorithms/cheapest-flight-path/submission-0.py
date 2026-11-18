from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # time: O(V * K + E) V is n, E len of flights
        # space: O(V * K + E)
        # method: BFS
        inf = float('inf')
        queue = deque()
        queue.append((src, 0))
        k += 1
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[src][0] = 0
        seen = set() # for edges
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))


        while queue:
            node, level = queue.popleft()
            for neighbor, price in graph[node]:
                if (node, neighbor) in seen or level + 1 > k or dist[neighbor][0] <= dist[node][level] + price:
                    continue
                dist[neighbor][level + 1] = min(dist[neighbor][level + 1], dist[node][level] + price)
                dist[neighbor][0] = min(dist[neighbor][0], dist[neighbor][level + 1])
                seen.add((node, neighbor))
                queue.append((neighbor, level + 1))
        
        if dist[dst][0] == inf:
            return -1
        return dist[dst][0]




