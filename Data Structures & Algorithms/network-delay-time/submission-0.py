from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time: O(V + E)
        # space: O(V)
        # method: BFS

        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        queue = deque()
        queue.append(k)
        inf = float("inf")
        dist = [inf] * (n + 1)
        dist[k] = 0
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    queue.append(neighbor)
        
        cost = max(dist[1:])

        if cost == inf:
            cost = -1
        return cost