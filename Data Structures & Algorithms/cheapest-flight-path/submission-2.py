class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # time: O(K * (V + E))
        # space: O(V)
        # method: Bellmon Ford
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp_dist = dist[:]
            for u, v, w in flights:
                if dist[u] + w < tmp_dist[v]: # level by level
                    tmp_dist[v] = dist[u] + w
            dist = tmp_dist[:]
        
        if dist[dst] == inf:
            return -1
        return dist[dst]